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
                [143, 120],
                [120, 32],
                [110, 40],
                [150, 40],
                [7**3, 7**3 - 7**2],
                [11**5, 11**5 - 11**4]]

        for d in data:
            calculated = phi(d[0])
            solution = d[1]
            self.assertEqual(calculated, solution)

if __name__ == '__main__':
    unittest.main()
