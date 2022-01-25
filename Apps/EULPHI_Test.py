import unittest
from EULPHI import phi

class EULPHI_Test(unittest.TestCase): #creating the class
    
    def test_phi(self):
        # [[input], [output]]
        data = [[0, 0],
                [7, 6],
                [49, 42],
                [35, 24],
                [63, 36],
                [150, 40]]

        for d in data:
            calculated = phi(d[0])
            solution = d[1]
            self.assertEqual(calculated, solution)

if __name__ == '__main__':
    unittest.main()
