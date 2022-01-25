import unittest
from BASES import db, bd

class BASES_Test(unittest.TestCase): #creating the class
    
    def test_db(self):
        # [[input], [output]]
        data = [[0, '0'],
                [3, '11'],
                [10, '1010'],
                [32, '100000'],
                [99, '1100011'],
                [1504, '10111100000']]

        for d in data:
            calculated = db(d[0])
            solution = d[1]
            self.assertEqual(calculated, solution)

    
    def test_bd(self):
        # [[input], [output]]
        data = [[0, '0'],
                [3, '11'],
                [10, '1010'],
                [32, '100000'],
                [99, '1100011'],
                [1504, '10111100000']]

        for d in data:
            calculated = bd('0b' + d[1])
            solution = d[0]
            self.assertEqual(calculated, solution)

if __name__ == '__main__':
    unittest.main()
