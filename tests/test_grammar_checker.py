import unittest
from app.grammar_checker import check_grammar
from io import BytesIO

class TestGrammarChecker(unittest.TestCase):
    def test_check_grammar(self):
        dummy_text = "This is a sentence with bad grammar This is another one"
        dummy_file = BytesIO(dummy_text.encode('utf-8'))
        result = check_grammar(dummy_file)
        self.assertGreater(result['grammar_errors'], 0)
        self.assertIsInstance(result['suggestions'], list)

if __name__ == "__main__":
    unittest.main()
