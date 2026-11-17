import unittest
from pathlib import Path


class TestHTML(unittest.TestCase):

    def test_index_contains_expected_heading(self):
        html = Path("index.html").read_text()

        self.assertIn(
            "<h1>Hello from Docker CI/CD!</h1>",
            html
        )


if __name__ == "__main__":
    unittest.main()
