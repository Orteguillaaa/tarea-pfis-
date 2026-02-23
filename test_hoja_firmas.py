
import unittest
import pandas as pd
import os
from hoja_firmas import process_students, format_groups

class TestSignatureSheet(unittest.TestCase):
    def setUp(self):
        # Create a mock CSV
        self.test_csv = 'test_students.csv'
        with open(self.test_csv, 'w') as f:
            f.write("Nombre; Apellido(s)\nZeta; Last\nAlpha; First\nBeta; Second")
            
    def tearDown(self):
        if os.path.exists(self.test_csv):
            os.remove(self.test_csv)

    def test_sorting(self):
        df = process_students(self.test_csv)
        self.assertEqual(df.iloc[0]['Nombre'], 'Alpha')
        self.assertEqual(df.iloc[-1]['Nombre'], 'Zeta')

    def test_grouping(self):
        df = process_students(self.test_csv)
        sheet = format_groups(df, group_size=2)
        # Should have 2 groups (3 students / size 2)
        self.assertIn("GRUPO 1", sheet)
        self.assertIn("GRUPO 2", sheet)

if __name__ == '__main__':
    unittest.main()
