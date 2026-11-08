# Summary — Directory of US/English Websites Accepting OUSD on Tempo

**Task:** TSK-JDXKJ9ZR · **Chain:** Tempo (4217) · **Last verification: 2026-11-08T22:19:46Z**

## Result

**2 verified websites** accept OUSD on Tempo for a good or service usable by
US/English customers:

1. **Taskmarket (https://taskmarket.dev/)** — gig/task marketplace; requesters
   fund escrow in OUSD on Tempo, workers are paid in OUSD. Confidence: high.
2. **PayI (https://www.payi.finance/)** — AI agent service; each prompt costs
   0.01 USD, paid in OUSD on Tempo via the Machine Payments Protocol.
   Confidence: high.

**51 leads were checked and excluded** (see `excluded-leads.csv`), including
Stripe (see below), BVNK, Ramp, Shopify, Coinbase, Deel, Mesh+Visa, Uniswap,
Morpho, and the full MPP merchant directory (which settles in USDC, not OUSD).

## Strongest limitations

- **The directory is small by design.** OUSD launched Sep 30, 2026 (~5 weeks
  ago); the public OUSD-on-Tempo surface is still almost entirely B2B rails.
  No conventional US retail/SaaS/e-commerce checkout accepting OUSD on Tempo
  was found by four independent search lanes, and Tempo's own OUSD page lists
  no merchants.
- **Stripe contradiction (most important negative finding):** Stripe's Sep 30
  announcement says businesses can "accept OUSD with Payments", but Stripe's
  live checkout docs list only USDC/USDP/USDG as customer-checkout tokens —
  OUSD is not listed. OUSD on Stripe is currently a treasury/payout/card
  asset, not a checkout token. Stripe is excluded, not listed.
- **No purchase was executed.** Checkout flows behind sign-in (PayI top-up,
  taskmarket task funding) are documented, not observed end-to-end.
- **Snapshot only.** Adoption is moving fast (BVNK went live Nov 6); new
  checkouts may appear within days of the 2026-11-08T22:19:46Z cutoff.
- **Self-reference disclosed:** this directory was itself commissioned as a
  Tempo/OUSD task on taskmarket.dev.

## Files

- `ousd-tempo-directory.csv` — 2 verified rows
- `report.md` — full report (method, results, exclusions, uncertainty)
- `excluded-leads.csv` — 51 excluded leads with reasons
- `regression_tests.py` + `regression_tests.csv` — 7/7 tests pass
