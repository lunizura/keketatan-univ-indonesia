# Contributing to Top Indonesian Universities Selectivity Platform

Thank you for contributing to the **Top Indonesian Universities Selectivity Platform & National Higher Education Database**. We welcome contributions from data analysts, educators, researchers, students, and software developers.

---

## 1. Development Principles & Code Standards

1. **Zero-Emoji Mandate:** All committed files, documentation, source code, data files, and Git commit messages must strictly contain zero emoji characters.
2. **Conventional Commits:** Use standard prefixes:
   - `docs:` for documentation, glossaries, admissions guides, or README updates.
   - `feat:` for new UI modules, interactive calculators, or dataset attributes.
   - `fix:` for data corrections, broken links, or calculation adjustments.
   - `test:` for test additions or validation assertions.
   - `chore:` for repository maintenance, dependencies, or configuration.
3. **Data Parity:** Any modification to university or study program records must be updated consistently across:
   - `data/ptn_keketatan.json`
   - `data/ptn_keketatan.js`
   - `data/ptn_keketatan.csv`
   - `data/metadata.json`

---

## 2. Mathematical Standards for Selectivity Metrics

When updating historical applicant numbers or daya tampung quotas:
- **Selectivity Percentage (`keketatan_persen`):**
  $$\text{Keketatan} = \left(\frac{\text{Daya Tampung}}{\text{Peminat}}\right) \times 100\%$$
  Must be rounded to exactly two decimal places.
- **Competition Ratio (`rasio_persaingan`):**
  Must follow the format `"1 : N"` where $N = \text{round}(\text{Peminat} / \text{Daya Tampung})$.

---

## 3. Local Development & Verification

Run the automated validation test suite before submitting any pull request:

```bash
# Execute unit tests across dataset integrity, DOM contracts, and zero-emoji compliance
python -m unittest discover tests
```

All 7 test cases must pass with `OK` status.

---

## 4. Pull Request Guidelines

1. Fork the repository and create a descriptive branch:
   ```bash
   git checkout -b docs/add-admissions-glossary
   ```
2. Verify all modifications locally using the test suite.
3. Reference official SNPMB BPPP Kemendikbudristek (`snpmb.bppp.kemdikbud.go.id`) or university admissions portals for data source citations.
