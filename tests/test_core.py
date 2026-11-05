import unittest
from bank_match_ambiguity.core import run
class DomainTests(unittest.TestCase):
 def test_two_matches(self):
  x=run({'invoices':[dict(id='A',cents=50),dict(id='B',cents=50),dict(id='C',cents=100)],'payments':[dict(id='P',cents=100)]});self.assertEqual(x['allocations_found'],2);self.assertFalse(x['unique_proven'])
 def test_nonreuse(self):self.assertEqual(run({'invoices':[dict(id='A',cents=100)],'payments':[dict(id='P',cents=100),dict(id='Q',cents=100)]})['allocations_found'],0)
 def test_unique(self):self.assertTrue(run({'invoices':[dict(id='A',cents=70)],'payments':[dict(id='P',cents=70)]})['unique_proven'])
