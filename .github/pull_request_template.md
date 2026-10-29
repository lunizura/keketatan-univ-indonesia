## Pull Request Overview

### Description of Changes
Please provide a summary of the dataset modifications, calculations, documentation, or analytical features included in this PR.

### Verification Checklist
- [ ] Ran `python -m unittest discover tests` and all 7 test cases passed cleanly.
- [ ] Verified strict zero-emoji compliance across all modified and newly added files.
- [ ] Confirmed mathematical consistency: `keketatan_persen == round((daya_tampung / peminat) * 100, 2)`.
- [ ] Maintained 4-way parity across `ptn_keketatan.json`, `ptn_keketatan.js`, `ptn_keketatan.csv`, and `metadata.json`.
- [ ] Cited official references from SNPMB BPPP (`snpmb.bppp.kemdikbud.go.id`) or university portals.
