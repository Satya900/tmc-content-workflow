"""Checks the copy linter against the writing standards' mechanical rules."""
import unittest
from lint_copy import check


def codes(text, level="ERROR"):
    return [m for _, l, m in check(text) if l == level]


class LintCopyTests(unittest.TestCase):
    def test_clean_copy_passes(self):
        text = "## Compare the exclusions\n\nAdd every excluded cost to the lower quotation. Compare the totals again.\n"
        self.assertEqual(check(text), [])

    def test_restricted_words_and_punctuation(self):
        found = codes("You can unlock value; it’s great — really!\n")
        for expected in ('restricted word "can"', 'restricted word "unlock"', "semicolon",
                         "curly quote", "em dash", "exclamation mark"):
            self.assertIn(expected, found)

    def test_format_rules(self):
        found = codes("---\n\nDear parents, see the trip. #SchoolTrips \U0001F680\n\nIn this article we look at costs. It is short.\n")
        for expected in ("markdown divider", "letter framing", "hashtag", "emoji", "setup phrase"):
            self.assertIn(expected, found)

    def test_placeholders_code_and_off_regions_ignored(self):
        text = ("Send it to [NEEDS INPUT: link that can change]. Use `that` here.\n\n"
                "<!-- lint: off -->\nThis can say that.\n<!-- lint: on -->\n")
        self.assertEqual(codes(text), [])

    def test_table_separator_is_not_a_divider(self):
        self.assertEqual(codes("| A | B |\n|---|---|\n| One item. | Two items. |\n"), [])

    def test_warnings(self):
        found = codes("## How To Compare School Trip Quotes\n\nIt is a signal, not a sign-up.\n", "WARN")
        self.assertIn("heading not in sentence case", found)
        self.assertIn("contrast pattern (X not Y, X but Y, rather than)", found)
        self.assertIn("one-sentence paragraph", found)


if __name__ == '__main__': unittest.main()
