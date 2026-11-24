import unittest
from catalogue import Concept, search

class CatalogueTests(unittest.TestCase):
    def setUp(self):
        self.a = Concept("Example A", "hypothesis", ("Learning",))
        self.b = Concept("Example B", "illustrative", ("systems",))
    def test_case_insensitive(self):
        self.assertEqual(search([self.a,self.b], "LEARNING"), [self.a])
    def test_status(self):
        self.assertEqual(search([self.a,self.b], "", "illustrative"), [self.b])
    def test_no_match(self):
        self.assertEqual(search([self.a], "unknown"), [])
    def test_invalid_status(self):
        with self.assertRaises(ValueError):
            search([self.a], "", "proven")
    def test_invalid_record(self):
        with self.assertRaises(ValueError):
            search([Concept("A","proven",())], "")

if __name__ == "__main__":
    unittest.main()
