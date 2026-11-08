#!/usr/bin/env python3
"""Regression tests for the OUSD-on-Tempo merchant directory.

Validates ousd-tempo-directory.csv:
  T1  required fields present and non-empty on every row
  T2  canonical URL syntax valid (http/https, host present)
  T3  no duplicate canonical URLs (normalized: lowercase host, strip trailing slash)
  T4  every row has OUSD evidence AND Tempo evidence (distinct excerpts recorded)
  T5  verification timestamp present, ISO-8601 UTC, and not in the future
  T6  confidence value in {high, medium, low}
  T7  canonical URL reachability (HTTP 200/3xx) where technically possible;
      failures are reported and must be explained in the report, not hidden
Usage: python3 regression_tests.py [--csv ousd-tempo-directory.csv]
Exit 0 = all tests pass. Prints a per-test PASS/FAIL summary.
"""
import csv
import re
import sys
import urllib.parse
from datetime import datetime, timezone

CSV_PATH = "ousd-tempo-directory.csv"

REQUIRED = [
    "merchant_name", "canonical_url", "category",
    "customer_region_evidence", "ousd_evidence", "tempo_evidence",
    "checkout_instructions", "verified_utc", "source_urls",
    "excerpts", "confidence", "caveats",
]

URL_RE = re.compile(r"^https?://[^/\s]+(/\S*)?$", re.IGNORECASE)
TS_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")


def norm_url(u: str) -> str:
    p = urllib.parse.urlparse(u.strip().lower())
    host = p.netloc
    if host.startswith("www."):
        host = host[4:]
    path = p.path.rstrip("/") or ""
    return f"{p.scheme}://{host}{path}"


def check_reachability(url: str, timeout: int = 15):
    """Best-effort HEAD then GET. Returns (ok, status_or_error)."""
    try:
        import requests
        try:
            r = requests.head(url, timeout=timeout, allow_redirects=True,
                              headers={"User-Agent": "Mozilla/5.0"})
            if r.status_code < 400:
                return True, r.status_code
        except Exception:
            pass
        r = requests.get(url, timeout=timeout, allow_redirects=True,
                         headers={"User-Agent": "Mozilla/5.0"})
        return r.status_code < 400, r.status_code
    except ImportError:
        return None, "requests unavailable"
    except Exception as e:
        return False, f"{type(e).__name__}: {e}"


def main():
    path = CSV_PATH
    if "--csv" in sys.argv:
        path = sys.argv[sys.argv.index("--csv") + 1]
    results = []
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    # T1 required fields
    missing = []
    for i, r in enumerate(rows, start=2):
        for col in REQUIRED:
            if col not in r or not (r[col] or "").strip():
                missing.append(f"row {i} col {col}")
    results.append(("T1 required fields non-empty",
                    not missing, "; ".join(missing) or f"{len(rows)} rows OK"))

    # T2 URL syntax
    bad = [r["canonical_url"] for r in rows
           if not URL_RE.match((r.get("canonical_url") or "").strip())]
    results.append(("T2 canonical URL syntax valid",
                    not bad, "; ".join(bad) or f"{len(rows)} URLs OK"))

    # T3 duplicates
    seen, dups = {}, []
    for r in rows:
        n = norm_url(r.get("canonical_url") or "")
        if n in seen:
            dups.append(f"{r.get('canonical_url')} dup of {seen[n]}")
        seen[n] = r.get("canonical_url")
    results.append(("T3 no duplicate canonical URLs",
                    not dups, "; ".join(dups) or "no duplicates"))

    # T4 OUSD + Tempo evidence
    weak = []
    for i, r in enumerate(rows, start=2):
        if len((r.get("ousd_evidence") or "").strip()) < 20:
            weak.append(f"row {i} OUSD evidence too short")
        if len((r.get("tempo_evidence") or "").strip()) < 20:
            weak.append(f"row {i} Tempo evidence too short")
    results.append(("T4 OUSD evidence AND Tempo evidence present",
                    not weak, "; ".join(weak) or "all rows have both"))

    # T5 timestamps
    now = datetime.now(timezone.utc)
    bad_ts = []
    for i, r in enumerate(rows, start=2):
        ts = (r.get("verified_utc") or "").strip()
        if not TS_RE.match(ts):
            bad_ts.append(f"row {i} bad format {ts!r}")
            continue
        try:
            dt = datetime.strptime(ts, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
            if dt > now:
                bad_ts.append(f"row {i} timestamp in future {ts}")
        except ValueError:
            bad_ts.append(f"row {i} unparsable {ts!r}")
    results.append(("T5 verification timestamps ISO-8601 UTC, not future",
                    not bad_ts, "; ".join(bad_ts) or "all timestamps OK"))

    # T6 confidence values
    bad_conf = [f"row {i} {r.get('confidence')!r}" for i, r in enumerate(rows, start=2)
                if (r.get("confidence") or "").strip().lower() not in ("high", "medium", "low")]
    results.append(("T6 confidence in {high, medium, low}",
                    not bad_conf, "; ".join(bad_conf) or "all confidences OK"))

    # T7 reachability (best effort)
    unreach = []
    for r in rows:
        ok, status = check_reachability((r.get("canonical_url") or "").strip())
        if ok is False:
            unreach.append(f"{r.get('canonical_url')} -> {status}")
        elif ok is None:
            unreach.append(f"{r.get('canonical_url')} -> check unavailable ({status})")
    results.append(("T7 canonical URLs reachable (HTTP <400)",
                    not unreach, "; ".join(unreach) or "all reachable"))

    failed = 0
    for name, ok, detail in results:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}")
        if not ok:
            failed += 1
    print(f"\n{len(results) - failed}/{len(results)} tests passed; "
          f"{len(rows)} directory rows checked.")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
