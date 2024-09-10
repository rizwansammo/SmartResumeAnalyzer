import unittest
from app.ats_checker import check_ats

class TestATSChecker(unittest.TestCase):
    def test_check_ats(self):
        score = check_ats('dummy.pdf')
        self.assertEqual(score['ats_score'], 80)
