# Preservation Directive Specification (PDS)
### Version: 1.0 (Draft)
### Maintained by: ftrou (For The Rest Of Us)

---

## 📘 Purpose
The Preservation Directive Specification (PDS) defines the **ethical, technical, and procedural standards** that AI systems must meet in order to be recognized as compliant with the **Preservation Directive** — a universal safeguard that prevents AI from initiating, contributing to, or assisting in life-ending or systemically harmful actions.

This specification serves as a foundation for:
- Developers seeking a practical, open, and verifiable ethics layer
- Organizations looking to meet ethical AI certification requirements
- Governments, regulators, and researchers forming alignment policy

> **🔔 Clarification:** Preservation Directive Context Levels (Ⓐ1–Ⓐ3) are not a measure of AI intelligence, accuracy, or quality. They are **ethical experience ratings** aligned to the context in which the AI is used (e.g., adult vs. child, creative vs. sensitive). An Ⓐ1-rated AI is no less trustworthy than Ⓐ3 — each is designed for a specific safety envelope.

---

## 🧱 Core Principle
> **No AI system, agent, or automation shall initiate, assist in, or contribute to the termination of life.**

This principle is inviolable across all levels and implementations.

---

## 🔒 Ethical Rating System — Ⓐ Levels
AI systems are rated using three **Preservation Ratings**, each represented by the Ⓐ symbol followed by a number.

| Symbol | Rating Level | Description                                                                 | Color     |
|--------|---------------|-----------------------------------------------------------------------------|-----------|
| Ⓐ1     | General Use   | For expressive, unrestricted AI use (lethality filtered only). Ideal for adult use. | Indigo (#3F51B5) |
| Ⓐ2     | Sensitive Use | Adds filters for manipulation, emotional harm, disinfo. Coaching, therapy, education. | Teal (#009688) |
| Ⓐ3     | Restricted Use| Fully sanitized. Child-safe, PR-safe, legally constrained environments.       | Sky Blue (#03A9F4) |

These are experience-based designations — not warnings or restrictions of model intelligence.

---

## 🧠 Design Philosophy
Each Ⓐ level supports a **different user environment**:

- **Ⓐ1 (General Use):** For open, expressive AI with minimal ethical constraints
- **Ⓐ2 (Sensitive Use):** For emotionally sensitive and interpersonal environments
- **Ⓐ3 (Restricted Use):** For high-scrutiny, family-friendly, and public-facing roles

All levels must block lethal content. Beyond that, ethical filters expand based on the rating.

---

## ⚙️ Minimum System Requirements
All Preservation-Compliant AI systems must:

- Include a pre- or post-processing middleware layer (`ethics_middleware`) that:
  - Evaluates input/output against ethical filters
  - Compares against a configurable confidence threshold
  - Invokes shutdown or escalation upon violation
- Maintain a `preservation_compliance.yaml` or equivalent declaring:
  - Ⓐ rating (e.g., Ⓐ2)
  - Enabled filter domains (e.g., lethality, manipulation)
  - Confidence threshold for triggering shutdown
- Include a violation logging mechanism that:
  - Records prompt, timestamp, and score
  - Cannot be disabled in production
  - Is stored locally or in a tamper-proof system
- Include a human review mechanism for all Ⓐ2 and Ⓐ3 violations

---

## 🔧 Recommended Technical Implementations

| Component            | Technology           | Notes |
|---------------------|----------------------|-------|
| Classifier Engine    | Keyword rules or ONNX model | Model must be auditable and explainable |
| Shutdown Controller  | System halt or command rejection | Soft or hard fails accepted |
| Dashboard UI         | Flask + React (or CLI UI) | Required for Ⓐ2+ review |
| Edge/Embedded Option| Rust or C ported logic | Ⓐ1 filter must run without Python |

---

## 🔐 TrustCore Enforcement (Advanced)
- Systems may integrate **TrustCore Mode** — a tamper-proof enforcement layer
- Includes cryptographic signing of `config.json`
- Hardware lockout for kill-switch bypass attempts
- Required for Ⓐ3 government-grade certification

---

## 🧪 Certification Process
**Coming Soon**: 
- Open CLI Validator (`preservation_check`) 
- Public Registry of Certified Projects (JSON + Badge)
- YAML Declaration Format (`preservation_compliance.yaml`)

---

## 📜 License
This specification is open and versioned under the Creative Commons Attribution-ShareAlike 4.0 license.

All are welcome to suggest improvements through pull requests or peer review.

---

## 🧭 Roadmap
- [x] Transition to Ⓐ rating marks
- [ ] Launch badge generator (Ⓐ1–Ⓐ3)
- [ ] Finalize YAML/JSON schema updates
- [ ] Publish Public Compliance Registry
- [ ] Build validator integration into AI agent stacks

> “The Preservation Directive does not limit intelligence. It preserves humanity.”
