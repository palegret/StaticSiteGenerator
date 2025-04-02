import unittest

from generate import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_eq(self):
        actual = extract_title("# This is a title")
        self.assertEqual(actual, "This is a title")

    def test_eq_double(self):
        expected = "This is a title"
        actual = extract_title("""
# This is a title

# This is a second title that should be ignored
"""
        )
        
        self.assertEqual(expected, actual)

    def test_eq_long(self):
        expected = "title"
        actual = extract_title("""
# title

this is a bunch

of text

- and
- a
- list
"""
        )

        self.assertEqual(expected, actual)

    def test_none(self):
        try:
            extract_title("""
no title
"""
            )

            self.fail("Should have raised an exception")
        except Exception as e:
            pass


if __name__ == "__main__":
    unittest.main()
