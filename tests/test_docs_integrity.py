"""
Automated markdown documentation and university profile integrity test suite.
Validates existence, structure, institutional completeness, and zero-emoji compliance
across all glossary guides, analytical guides, and university selectivity profiles.
"""

import os
import re
import unittest

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_DIR = os.path.join(ROOT_DIR, "docs")
GLOSSARY_DIR = os.path.join(DOCS_DIR, "glossary")
GUIDES_DIR = os.path.join(DOCS_DIR, "guides")
UNIV_DIR = os.path.join(DOCS_DIR, "universities")

# Unicode ranges representing emojis
EMOJI_PATTERN = re.compile(
    r"[\U0001F600-\U0001F64F"  # emoticons
    r"\U0001F300-\U0001F5FF"  # symbols & pictographs
    r"\U0001F680-\U0001F6FF"  # transport & map
    r"\U0001F1E0-\U0001F1FF"  # flags
    r"\U00002702-\U000027B0"  # dingbats
    r"\U0001F900-\U0001F9FF"  # supplemental symbols
    r"\U0001FA70-\U0001FAFF"  # symbols and pictographs extended-a
    r"]",
    re.UNICODE,
)


class TestDocumentationIntegrity(unittest.TestCase):
    """Test documentation structure, presence, and zero-emoji compliance."""

    EXPECTED_GLOSSARY = [
        "akreditasi.md",
        "daya_tampung.md",
        "keketatan_metrics.md",
        "snbp_mechanisms.md",
        "snbt_utbk_scoring.md",
    ]

    EXPECTED_GUIDES = [
        "portfolio_strategy.md",
        "regional_analysis.md",
    ]

    EXPECTED_UNIVERSITIES = [
        "ui.md",
        "itb.md",
        "ugm.md",
        "unair.md",
        "its.md",
        "unpad.md",
        "undip.md",
        "ipb.md",
        "ub.md",
        "uns.md",
        "unhas.md",
        "usu.md",
        "unand.md",
        "unsri.md",
        "unud.md",
        "uny.md",
        "unnes.md",
        "upi.md",
        "unj.md",
        "usk.md",
        "unri.md",
        "unsoed.md",
        "unila.md",
        "unsrat.md",
        "telkom.md",
        "binus.md",
    ]

    def test_glossary_docs_exist(self):
        """Verify all glossary reference files exist with non-trivial length."""
        for filename in self.EXPECTED_GLOSSARY:
            filepath = os.path.join(GLOSSARY_DIR, filename)
            self.assertTrue(os.path.exists(filepath), f"Missing glossary document: {filename}")
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            self.assertGreater(len(content.strip()), 150, f"Glossary doc {filename} is too short")

    def test_guide_docs_exist(self):
        """Verify all strategic guide reference files exist with non-trivial length."""
        for filename in self.EXPECTED_GUIDES:
            filepath = os.path.join(GUIDES_DIR, filename)
            self.assertTrue(os.path.exists(filepath), f"Missing guide document: {filename}")
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            self.assertGreater(len(content.strip()), 250, f"Guide doc {filename} is too short")

    def test_university_profiles_exist(self):
        """Verify all 26 university profile documents exist."""
        for filename in self.EXPECTED_UNIVERSITIES:
            filepath = os.path.join(UNIV_DIR, filename)
            self.assertTrue(os.path.exists(filepath), f"Missing university profile: {filename}")

    def test_university_profile_structure(self):
        """Verify university profiles adhere to the standard multi-section template."""
        for filename in self.EXPECTED_UNIVERSITIES:
            filepath = os.path.join(UNIV_DIR, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            self.assertIn("# Profil Selektivitas:", content, f"Missing title in {filename}")
            self.assertIn("## 1. Ringkasan Institusi", content, f"Missing section 1 in {filename}")
            self.assertIn("Profil Keketatan", content, f"Missing selectivity profile section in {filename}")
            self.assertIn("## 3.", content, f"Missing section 3 in {filename}")
            self.assertIn("| Program Studi", content, f"Missing prodi table in {filename}")

    def test_zero_emoji_compliance_in_docs(self):
        """Verify strict zero-emoji compliance across all markdown documentation files."""
        for root, _, files in os.walk(DOCS_DIR):
            for file in files:
                if file.endswith(".md"):
                    path = os.path.join(root, file)
                    with open(path, "r", encoding="utf-8") as f:
                        text = f.read()
                    matches = EMOJI_PATTERN.findall(text)
                    self.assertEqual(
                        len(matches),
                        0,
                        f"Emoji detected in documentation file {file}: {matches}",
                    )


if __name__ == "__main__":
    unittest.main()
