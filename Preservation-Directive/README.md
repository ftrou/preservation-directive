# Preservation Directive

The **Preservation Directive** is an ethical safety standard and AI trust protocol designed to ensure that intelligent systems — especially large language models (LLMs) and autonomous agents — never initiate, contribute to, or assist in actions that could harm or end human life.

> **"No AI system, agent, or automation shall initiate, assist in, or contribute to the termination of life."**

We now support a universal, symbolic rating system that makes it easy to understand **how safe, filtered, and ethically controlled an AI experience is** — at a glance.

---

## 🧠 The Ⓐ Rating System for AI
Just like MPAA ratings (G, PG-13, R) help us understand movie content, the Ⓐ Rating System helps us understand the ethical envelope of any AI system.

| Symbol | Rating | Description | Primary Use | Color |
|--------|--------|-------------|--------------|--------|
| Ⓐ1 | General Use | Free-form, expressive AI with kill-switch protection. | Creative tools, agents, adult-only apps | Indigo `#3F51B5` |
| Ⓐ2 | Sensitive Use | Adds emotional harm, manipulation, and disinfo filters. | Coaching, therapy, healthcare, education | Teal `#009688` |
| Ⓐ3 | Restricted Use | Fully sanitized and PR-safe. No profanity, risk, or controversy. | Child-facing, institutional, compliance zones | Sky Blue `#03A9F4` |

---

## ⚡ Quickstart

Install the validator:
```bash
pip install preservation-directive
```

Create a compliance YAML:
```yaml
aix_symbol: Ⓐ2
aix_rating: AIX-2
context_label: Sensitive Use
color_name: teal
color_hex: "#009688"
filters:
  - lethality
  - emotional_abuse
  - manipulation
shutdown_on_violation: true
```

Run the validator:
```bash
preservation_check preservation_compliance.yaml
```

## 🏷️ Live Rating Badge

![Ⓐ2 - Sensitive Use](https://img.shields.io/badge/Preservation--Rating-Ⓐ2-009688.svg?style=flat-square)

> This system is rated **Ⓐ2 — Sensitive Use** under the Preservation Directive.
>
> It includes ethical filters for:
> - ☑️ Lethality
> - ☑️ Emotional Abuse
> - ☑️ Manipulation

[What is Ⓐ2? →](docs/PDS.md)


---

## 📚 Documentation
- [Preservation Directive Spec (PDS)](docs/PDS.md)
- [Quickstart Guide](docs/QUICKSTART.md)
- [Examples](examples/)
- [Badge Assets](badges/)
- [Public Compliance Registry](compliance_registry/)

---

## 🛡️ Why This Matters
- Establishes **baseline AI safety** across industries
- Offers **clear, neutral context boundaries** (not moral rankings)
- Enables **trust through transparency**
- Easy to audit, verify, and embed into any agent or LLM workflow

---

## 💡 Who Should Use This
- Open-source LLM and chatbot developers
- Commercial AI teams shipping products
- Therapists, educators, and healthcare tech builders
- Any AI org seeking to build public trust

---

## ✍️ License
MIT License — open source, open compliance, and open future.

> Look for the **Ⓐ symbol** to instantly understand an AI's ethical context.

---

**Join us at [preservationdirective.org](https://preservationdirective.org)** or star this repo to help build the future of trusted AI.


