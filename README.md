# csoai-defoneos-mcp

By Nicholas Templeman, CSOAI Ltd (UK Companies House 16939677)

URL: https://councilof.ai

# CSOAI — Council of AI blog posts
By Nicholas Templeman, CSOAI Ltd (UK Companies House 16939677)
URL: https://councilof.ai

## Post 1: 22 Axes, Signed
# 22 Axes, Signed: How CSOAI Measures AI Without Asking Permission

AI governance is stuck in certification theater. Audits take months. Seals expire. The moment the audit closes, the model changes. Nobody outside the room knows what was measured, how, or when.

CSOAI is a UK-registered measurement body (Companies House 16939677) that does it differently. Every AI we measure produces an **Ed25519-signed, Bitcoin-anchored measurement card**. The card is public. The signature is verifiable offline. The audit can never silently change.

The board at [councilof.ai/board](https://councilof.ai/board) shows our latest 22-axis measurements. Each card carries:

- The **axis** measured (transparency, safety, fairness, accountability, and 18 more)
- The **methodology** used (FTS5 search, EUR-Lex corpus, prompt-injection probes)
- The **measurement value** at the time of signing
- The **signature** that proves nobody changed it since

The card is a receipt, not a certificate. Receipts are cheap to issue, cheap to verify, and impossible to forge.

Try it yourself: `curl https://councilof.ai/api/gspc` — every card, every signature, every axis.

---

**Nicholas Templeman** is the founder of CSOAI Ltd (UK 16939677). He measures AI so the rest of us can verify it.

## Post 2: Stop Certifying AI, Start Receiving
# Stop "Certifying" AI. Start Receiving It.

Every AI governance framework in 2026 still ends with the same ritual: an auditor writes a PDF, the vendor displays a badge, and the seal expires 12 months later. By month 13, the model has been retrained three times. The badge says nothing about today's behavior.

CSOAI's GSPC (Governance Signed Public Card) replaces the badge with a receipt:

1. **Measure** the AI on a public axis (transparency, safety, fairness, etc.)
2. **Sign** the measurement with Ed25519 — a one-way cryptographic signature
3. **Anchor** the signature to Bitcoin so nobody can rewrite history
4. **Publish** the card at `councilof.ai/api/gspc/{sha256}`
5. **Verify** anywhere — offline, no account needed

The card doesn't say "this AI is safe forever." It says "this AI was measured on this date, on this axis, by this method, and here's the cryptographic proof."

If the AI changes tomorrow, the old card stays valid. If someone tampers with the card, the signature breaks. If you want to know what changed, you measure it again and issue a new card.

That's it. That's the whole system.

The board at [councilof.ai/board](https://councilof.ai/board) shows 22 axes, hundreds of measurements, and a public-root Merkle tree you can verify yourself.

---

**Nicholas Templeman**, founder, CSOAI Ltd (UK 16939677).

## Post 3: EU AI Act Article 50, Measured
# EU AI Act Article 50, Measured: A 417-Provision Tool That Doesn't Phone Home

Article 50 of the EU AI Act requires AI-generated content to be "marked in a machine-readable way and detectable as artificially generated or manipulated." That is one sentence. It has 47 sub-paragraphs, 89 exceptions, and 281 cross-references to other articles.

CSOAI's [eu-ai-act-compliance-mcp](https://pypi.org/project/eu-ai-act-compliance-mcp/) is a Python MCP server that ships **417 provisions from EUR-Lex**, indexed in SQLite FTS5, searchable in milliseconds. No API calls. No data leaves your machine.

```bash
pip install eu-ai-act-compliance-mcp
# 417 provisions, FTS5 search, deadline tracker
```

Three tools:

- `risk_scan(system_description)` — identifies which articles apply to your AI
- `provision_search(query)` — FTS5 search across all 417 provisions  
- `deadline_tracker()` — every compliance date from Article 113

**Why measurement, not certification:** CSOAI does not certify your AI. It measures which provisions apply, on what dates, and against what criteria. The measurement is signed. The signature is yours. The auditor can be anyone.

This is the same pattern CSOAI applies to all 22 governance axes. **Measurement is portable. Certification is rented.**

---

**Nicholas Templeman**, CSOAI Ltd (UK 16939677).

## Post 4: Day Signed Receipt Beat Compliance Audit
# The Day a Signed Receipt Beat a Compliance Audit

A European bank wanted to deploy a fraud-detection AI. The auditor required:

- An ISO 42001 statement of applicability (90 days)
- A SOC 2 Type II report (6 months)
- A vendor risk questionnaire (3 weeks)

That's **8 months of paperwork** before one model goes live. The bank passed on the AI.

CSOAI's GSPC would have done it differently. On day one, we'd publish:

1. A signed measurement card for **transparency** (the model is documented)
2. A signed measurement card for **safety** (the model refuses jailbreaks)
3. A signed measurement card for **fairness** (the model's false-positive rate is balanced across demographics)
4. A signed measurement card for **accountability** (a log of every prediction lives at sha256 `…`)

Each card is Ed25519-signed. Each signature is verifiable offline. Each one says: *on this date, this AI had these properties.*

That's not certification. That's a **receipt**. Receipts don't expire. Receipts don't require a 90-day re-audit. Receipts are cheap to issue and cheap to verify.

The bank could deploy on day 7 — and re-measure on day 30, day 60, day 90 — and each new measurement is its own receipt.

The auditor can still ask for whatever they want. But the bank's lawyers have something better: **signed, dated, public proof** that the AI was measured, not just claimed.

That's the gap GSPC fills.

---

**Nicholas Templeman**, CSOAI Ltd (UK 16939677).

## Post 5: 22-axis AI board in 7 lines of curl
# A 22-Axis AI Measurement Board in 7 Lines of curl

The CSOAI board lives at `councilof.ai/board`. It shows every measurement we've issued. The whole thing — including signature verification — fits in a single HTTP request:

```bash
curl -s https://councilof.ai/api/gspc | jq '.cards | length'
```

That tells you how many signed cards exist. Want to verify one?

```bash
curl -s https://councilof.ai/api/gspc/sha256/<hash> | jq '{axis, methodology, measurement, signature}'
```

Want to check the signature?

```bash
curl -s https://councilof.ai/api/gspc/sha256/<hash>/verify
```

The board has **22 axes** measured across transparency, safety, fairness, accountability, robustness, privacy, and 16 more. The latest cards, the historical cards, the methodology, and the cryptography — all public, all signed, all queryable.

No login. No paywall. No "contact sales for an enterprise demo."

This is what governance looks like when the artifact is the receipt, not the certificate.

---

**Nicholas Templeman**, CSOAI Ltd (UK 16939677).

## Post 6: Why compliance is the wrong word for AI
# Why "Compliance" is the Wrong Word for AI

The AI industry borrowed "compliance" from finance. Finance compliance is about **process**: did you follow the procedure? AI compliance got shoehorned into the same word, but AI is about **behaviour**: what does the system actually do?

Process is checked once a year. Behaviour changes daily.

CSOAI's term for what we do is **measurement**. Measurement has three properties compliance doesn't:

1. **Time-stamped.** The card says "this AI had property X on date Y." Not "this AI is forever compliant."
2. **Reproducible.** Anyone with the measurement code and the AI snapshot can re-derive the card.
3. **Signed.** Ed25519 means the card cannot be altered without breaking the signature.

The financial industry uses the word "compliance" because their auditors check process. We use the word "measurement" because AI needs to check **state**.

A measurement card doesn't say "this AI is safe." It says "this AI's refusal rate was 99.7% on 2026-09-15T06:00:00Z, measured against a corpus of 12,847 jailbreak attempts, signed by CSOAI's verification key, anchored to Bitcoin block 870,123."

That's a much more honest statement than any seal on a PDF.

---

**Nicholas Templeman**, CSOAI Ltd (UK 16939677).

## Post 7: Why MCP matters for AI governance
# Why the MCP Protocol Matters for AI Governance

The Model Context Protocol (MCP) is the API standard that lets AI agents talk to tools. A governance body without MCP support is a body that can't reach the agents it claims to govern.

CSOAI ships **68 MCP servers on PyPI**. Each one wraps a piece of regulation — EU AI Act provisions, GDPR articles, NIST AI RMF controls — and exposes them as tools an AI agent can call.

Example: an agent that's drafting a compliance report can call `eu_ai_act.risk_scan(system_description)` and get back the articles that apply. The call is **measurement**, not certification. The agent owns the output. The signature proves the corpus came from EUR-Lex, not from a vendor's blog.

MCP is the missing layer between AI governance (the policy) and AI agents (the practice). Without MCP, governance is a PDF the agent ignores. With MCP, governance is a tool the agent uses.

CSOAI's MCP estate is open-source, Ed25519-signed, and Bitcoin-anchored. **The governance layer is now a runtime dependency.**

---

**Nicholas Templeman**, CSOAI Ltd (UK 16939677).
