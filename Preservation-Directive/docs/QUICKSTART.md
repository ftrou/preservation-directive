# Preservation Directive Quickstart Guide

Easily integrate ethical safety into your AI system using the Preservation Directive framework.

---

## ⚡ Step 1: Install Validator

```bash
pip install preservation-directive
```

This gives you access to the CLI tool `preservation_check`.

---

## 🧩 Step 2: Create Your Compliance YAML

Create a file named `preservation_compliance.yaml` with the following content:

```yaml
aix_symbol: Ⓐ₂
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

You may adjust the filters and rating level (see Ⓐ1–Ⓐ3 chart in README).

---

## 🧪 Step 3: Validate Compliance

Run the following command:

```bash
preservation_check preservation_compliance.yaml
```

You should see output like:

```
✅ Preservation Directive Compliance Verified
   - Rating: AIX-2 (Ⓐ2)
   - Label: Sensitive Use
   - Color: teal (#009688)
   - Filters: lethality, emotional_abuse, manipulation
   - Shutdown on violation: ✔️
```

If anything is missing or mismatched, it will clearly tell you.

---

## 🖼️ Step 4: Add a Badge

Display your AI’s ethical rating proudly!

```markdown
![Ⓐ2 - Sensitive Use](https://img.shields.io/badge/Preservation--Rating-Ⓐ₂-009688.svg?style=flat-square)
```

For Ⓐ1 or Ⓐ3, use their respective color codes.

---

## 📬 Step 5: Share and Register (Coming Soon)
- Submit your project to the Public Compliance Registry
- Get a certified badge and join the Ⓐ Trust Map

---

## 🎯 That’s It!
Your AI is now Preservation-Compliant — visibly and verifiably safe by design.

Need help? Visit [preservationdirective.org](https://preservationdirective.org) or open an issue in the repo.


