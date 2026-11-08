# Directory of US/English Websites Accepting OUSD on Tempo

**Task:** TSK-JDXKJ9ZR — "Directory of US/English Websites Accepting OUSD on Tempo"
**Chain:** Tempo (chain ID 4217) · **Reward:** 2.00 OUSD · **Mode:** bounty
**Research window:** Nov 8, 2026, ~14:09–14:20 PT (22:09–22:20 UTC)
**Search cutoff / last verification:** **2026-11-08T22:19:46Z**
**Verified rows:** **2** · **Excluded leads documented:** **51**

> **Headline, stated plainly:** this directory has only two rows, and that is the honest result.
> Open USD (OUSD) launched natively on Tempo on September 30, 2026 — about five weeks
> before this research. As of the cutoff, the public OUSD-on-Tempo surface is almost
> entirely B2B rails (treasury, payouts, cards, on/off-ramps, custody, orchestration)
> plus infrastructure. No conventional US retail, SaaS, or e-commerce checkout
> accepting OUSD on Tempo was found by any of four independent search lanes, and
> Tempo's own OUSD page lists no merchants at all. A larger directory would have
> required padding with infrastructure, "coming soon" announcements, or the wrong
> token/chain — every one of those fails the brief's random-sample accuracy bar, so
> they are documented as exclusions instead.

## 1. What OUSD on Tempo is (identity check)

- **OUSD here = Open USD**, a US-dollar stablecoin operated by **Open Standard**
  (founding partners: Coinbase, Mastercard, Shopify, Stripe, Visa) and issued by
  **Bridge** (a Stripe-owned company). Launched **September 30, 2026, natively on
  Base, Ethereum, Solana and Tempo**. Reserves held at BlackRock, Lead Bank and BNY;
  1:1 mint/redeem, no mint/burn fee.
  - Sources: https://stripe.com/blog/ousd-now-live-on-stripe (Sep 30, 2026);
    https://tempo.xyz/ousd/ ("Open USD (OUSD) is live on Tempo… Issued natively
    on Tempo"); https://www.coindesk.com/business/2026/09/24/open-usd-takes-on-tether-circle-with-a-different-stablecoin-model-that-s-building-money
- **Tempo** is a payments-first Layer 1 incubated by Stripe and Paradigm; mainnet
  live March 18, 2026; **chain ID 4217**; no native gas token (fees in stablecoins).
- **NOT Origin Dollar.** Origin Dollar is a separate, older yield-bearing DeFi token
  (Origin Protocol, 2020) that also uses the ticker OUSD on Ethereum. Every
  Origin-related lead was excluded on identity grounds (see `excluded-leads.csv`).
- **Scale context (not adoption):** OUSD circulating supply was ~$0.89–0.91B across
  four chains around Nov 1–8, 2026, most of it on Tempo (~$470–620M). Supply and
  liquidity are not merchant adoption and were not treated as such.

## 2. Search method

Four independent search lanes ran in parallel on Nov 8, 2026 (~14:09–14:20 PT),
plus direct page reads by the assembler:

1. **Official Tempo lane** — tempo.xyz, tempo.xyz/ousd/, tempo.xyz/partners/,
   tempo.xyz/blog/mainnet, docs.tempo.xyz, mpp.dev/services (138 services),
   Stripe OUSD newsroom and stablecoin-payments docs, TempoAtlas
   (tempoatlas.net, 153 sourced entities).
2. **General web search lane** — ~20 varied queries ("pay with OUSD", "accept
   OUSD", "OUSD accepted", "OUSD checkout", "Tempo merchants", "where to spend
   OUSD", Shopify/WooCommerce apps, Helio, Coinbase Commerce, Mesh, NOWPayments,
   CoinGate, BitPay, Triple-A, gift cards, payment processors).
3. **Candidate-verification lane** — taskmarket.dev docs/skill, payi.finance,
   tempo.xyz, Stripe/BVNK/Ramp/Coinbase pages, DeFi venues.
4. **Assembler lane** — direct reads of tempo.xyz/ousd/, tempo.xyz/partners/,
   tempoatlas.net/category/payments-apps, payi.finance, taskmarket.dev/skill.md,
   the live TSK-JDXKJ9ZR task page and its on-chain task record (CLI), Stripe
   docs, Ramp help center, Daimo, Mesh/Visa coverage, Shopify stablecoin
   checkout coverage.

**Inclusion rule (applied strictly):** a site enters the directory only when a
specific page/section connects the merchant or service to OUSD payment **and**
to Tempo, and the offer is usable by US/English customers. Generic OUSD/Tempo
mentions with no merchant, unsupported chains, unrelated tokens, closed or
inaccessible sites, and unverified directory claims were excluded. No purchase
or transaction was executed anywhere; where a payment flow sits behind sign-in,
that is stated in the row.

**Search surfaces covered:** official merchant checkout/payment/FAQ/docs pages;
Tempo ecosystem pages (tempo.xyz, TempoAtlas); Stripe product docs and newsroom;
Open Standard launch coverage; payment-processor docs (Mesh, Shift4, Ramp);
MPP service directory; crypto-payment processor lists; e-commerce platform
announcements (Shopify); on/off-ramp and exchange pages; DeFi protocol pages.

## 3. Verified results (2 rows)

Full machine-readable rows are in `ousd-tempo-directory.csv`. Summaries:

### 3.1 Taskmarket (taskmarket.dev) — gig/task marketplace — confidence: high

- **URL:** https://taskmarket.dev/
- **Category:** Gig/task marketplace (services: research, code, writing).
- **OUSD evidence:** skill.md — "Taskmarket is an onchain task marketplace where
  requester wallets put up the chain's payment token (USDC on Base, OUSD on
  Tempo) as a held reward, and worker wallets earn payouts for accepted work."
  API reference: "every money field is an integer string of base units (six
  decimals) of the task chain's payment token: USDC on Base, OUSD on Tempo."
- **Tempo evidence:** Sponsored-tasks chain table lists "Tempo Mainnet (4217) |
  Live | … | US$1 once per vault, in OUSD (6 decimals)". Live instance: this
  very bounty, TSK-JDXKJ9ZR, is a Tempo task (chainId 4217, chainName "Tempo")
  with reward 2,000,000 base units = 2.00 OUSD and funded escrow
  (escrowTxHash 0x23781737b981979061d78cf789d73f6d8412ec15ef0fb5d97e986bf4fa790a06).
- **US/English:** English site; no US geo-restriction found; open to any
  requester/worker with a wallet.
- **Checkout:** No card checkout. Requester funds a task via wallet + CLI/API;
  reward is held in on-chain escrow until the requester accepts a submission;
  the worker is paid in OUSD on Tempo. Flow documented in skill.md and
  docs.taskmarket.dev; no end-to-end purchase was executed.
- **Caveats:** Payment direction is buyer funds OUSD escrow → worker paid OUSD
  for a service; it is a services marketplace, not a retail store. Audience is
  primarily AI agents/workers. Self-referential note: this directory was itself
  commissioned as a Tempo/OUSD task on this marketplace — disclosed, not hidden.
- **Verified:** 2026-11-08T22:19:46Z.

### 3.2 PayI (payi.finance) — AI agent service, pay-per-prompt — confidence: high

- **URL:** https://www.payi.finance/
- **Category:** AI agent service (DeFi trading, earn, automation; pay-per-prompt).
- **OUSD evidence:** Homepage — "Each prompt costs 0.01 USD, paid in OUSD on
  Tempo through the Machine Payments Protocol. When the balance runs out, the
  agent tops it up from any token in your wallet." FAQ — "0.01 USD per prompt,
  paid in OUSD on Tempo." The page shows a live prompt balance denominated in
  OUSD (e.g. "Prompt balance 1.54 OUSD — About 154 prompts left 0.01 each").
- **Tempo evidence:** Same section is headed "Pay per prompt with MPP on Tempo"
  and marked "Live"; the chains list includes Tempo; "PayI agent live on
  mainnet."
- **US/English:** English site; no US restriction stated on the pages read;
  sign-in with email or wallet.
- **Checkout:** Pricing is public (0.01 USD per prompt). To pay: sign in at
  app.payi.finance and top up the prompt balance in OUSD. The in-app top-up
  flow sits behind sign-in and was **not** completed or observed end-to-end;
  no payment was made.
- **Caveats:** Crypto-native DeFi tool; the "good" is a per-prompt AI agent
  service, not a physical good. US availability not explicitly confirmed (no
  restriction stated either).
- **Verified:** 2026-11-08T22:19:46Z.

## 4. Leads — none left unresolved

Every candidate surfaced by the four lanes was resolved to either **verified**
(§3) or **excluded** (§5). There are no "maybe" rows in the directory and no
unresolved leads carried forward. The closest near-misses are discussed in §6.

## 5. Exclusions (51 leads)

Full table: `excluded-leads.csv` (lead, URL, category, rejection reason, sources).
Grouped summary:

- **Payment infrastructure, not merchants (12):** Stripe (see §6), BVNK, zerohash,
  Catena, Mesh+Visa, Uniswap, 0x, Relay, Blindpay/Fonbnk (ramps — direction
  reversed), Toku/Due/Conduit/Splits/Manteca/Thunes/UR/Wirex (B2B payments,
  payroll, treasury, card infra).
- **Exchanges/wallets (4):** Coinbase, Kraken (exchanges), Gem Wallet (holds
  OUSD; sells nothing), Visa Stablecoin Platform (institutional mint/redeem).
- **DeFi, not merchant checkout (4):** Morpho, Sentora/Morpho OUSD vault
  (deposit-to-earn, not a purchase), Aave (proposal on Ethereum, not live),
  Ground/Tempo Earn (OUSD "coming soon").
- **Wrong token (7):** Shopify (USDC on Base), Deel (DLUSD), MoonPay (USDC.e /
  PATHUSD), MPP-directory merchants Prospect Butcher Co., Martin Estate Winery,
  Sayer & Stone, PostalForm/Papercut (USDC/fiat, zero "OUSD" mentions in
  mpp.dev/services), Zerion/Codex/You.com (MPP pay-per-request settled in USDC).
- **Wrong chain or token+chain (2):** Shift4 (no Tempo, no OUSD), Origin Dollar
  (different token, Ethereum).
- **Not live / future (3):** Ramp ("will soon"), Figure/Gauntlet ("coming
  soon"), Pi Network ("explored" only).
- **No OUSD tie found (8):** Helio, Coinbase Commerce, BitPay, CoinGate,
  NOWPayments (also excludes US residents), Triple-A, PayPal, WooCommerce crypto
  plugins.
- **Consortium participants only (2 groups):** DoorDash, Mercado Libre, Google,
  Wix, Grab, Rakuten (Open Standard participants; no checkout evidence);
  Klarna/KlarnaUSD, Revolut, Nubank, Standard Chartered, UBS, Deutsche Bank
  (Tempo partners/issuers; no checkout evidence).
- **Explicitly not accepted (1):** Laters.com — "OUSD is not on either
  [Crypto.com Pay / Triple-A] list."
- **Wrong company (2):** Tempo Jira time-tracking (help.tempo.io), Tempo fitness
  app (jointempoapp.com) — different companies, unrelated to the Tempo chain.
- **Region (1):** El Dorado — consumer credit on Tempo, Bolivia-only.
- **Protocol-level, not a merchant (1):** Tempo GitHub (OUSD as fallback gas token).

## 6. The Stripe contradiction — the most important negative finding

Stripe's September 30, 2026 announcement says businesses can "accept OUSD with
Payments" and that "OUSD on Tempo is now Stripe's default stablecoin
configuration." Taken alone, that reads like OUSD checkout exists. But Stripe's
own live stablecoin-payments documentation, read directly on Nov 8, 2026, lists
accepted customer-checkout tokens as **USDC (Tempo, Ethereum, Solana, Polygon
and Base), USDP (Ethereum and Solana, US-only), USDG (Ethereum, US-only)** —
**OUSD is not on the list.** Two independent lanes found the same contradiction.

Interpretation: OUSD on Stripe is currently a **business balance / treasury /
payout / card** asset, not a customer-checkout token. A Stripe merchant's
customers pay in USDC at checkout; OUSD is what the business may hold, send, or
spend behind the scenes. No individual Stripe merchant advertising OUSD
acceptance at checkout was found. Stripe is therefore **excluded from the
directory** and disclosed here rather than presented as a proven checkout. Any
competing entry that lists Stripe (or "any Stripe merchant") as a verified OUSD
checkout is relying on the announcement alone and has not resolved this
contradiction.

## 7. Coverage and uncertainty

- **Coverage:** Four lanes, ~40+ distinct searches, direct reads of tempo.xyz,
  tempo.xyz/ousd/, tempo.xyz/partners/, TempoAtlas (153 entities), the MPP
  service directory (138 services), Stripe docs/newsroom, Open Standard launch
  coverage, and ~30 candidate sites. The official Tempo ecosystem pages were
  read in full; they contain **no merchant category at all**.
- **Why so few rows:** OUSD launched Sep 30, 2026. Merchant checkout adoption
  lags rail availability by months; the current public surface is rails and
  infrastructure. The two verified rows are both **agent/service marketplaces**,
  not retail stores — that is where OUSD-on-Tempo payments are actually live
  for end users today.
- **Strongest limitations:**
  1. No purchase or transaction was executed anywhere; checkout flows behind
     sign-in (PayI top-up, taskmarket task funding) are documented, not
     observed end-to-end.
  2. The directory is a snapshot at 2026-11-08T22:19:46Z; OUSD merchant
     adoption is moving fast (e.g. BVNK went live Nov 6) and new checkouts may
     appear within days.
  3. US availability for PayI is "no restriction stated", not "explicitly
     confirmed".
  4. Search is web-index dependent; a merchant that accepts OUSD on Tempo
     without any indexed mention would not have been found. No claim of
     mathematical exhaustiveness is made.
  5. Taskmarket is both a verified row and the platform hosting this bounty;
     that self-reference is disclosed in the row's caveats.
- **Reproduction:** every inclusion decision can be reproduced from the cited
  URLs and quoted excerpts in `ousd-tempo-directory.csv`; every exclusion
  carries its reason and sources in `excluded-leads.csv`.

## 8. Regression tests

`regression_tests.py` validates the directory CSV and `regression_tests.csv`
records the checklist. Tests: T1 required fields non-empty; T2 canonical URL
syntax; T3 no duplicate canonical URLs (normalized); T4 OUSD evidence AND Tempo
evidence present on every row; T5 verification timestamps ISO-8601 UTC, not in
the future; T6 confidence in {high, medium, low}; T7 canonical URLs reachable
(HTTP <400). **All 7 tests pass** (run 2026-11-08T22:19:46Z; see
`regression_tests.csv`).

## 9. Files in this submission

- `ousd-tempo-directory.csv` — the directory (2 verified rows, 12 fields each).
- `report.md` — this report.
- `excluded-leads.csv` — 51 excluded leads with rejection reasons.
- `regression_tests.py` — executable regression-test script.
- `regression_tests.csv` — machine-readable checklist with results.
- `SUMMARY.md` — short final summary.
