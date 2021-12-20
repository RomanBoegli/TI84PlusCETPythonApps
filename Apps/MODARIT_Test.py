import unittest
import numpy as np
from MODARIT import egcd, mod, modinv, mmodinv

class MODARIT_Test(unittest.TestCase): #creating the class
    
    def test_egcd(self):
        # [[input], [output]]
        data = [[[0, 0], [0, 0, 1]],
                [[5, 8], [1, -3, 2]],
                [[22, 49], [1, -20, 9]],
                [[30, 498], [6, -33, 2]]]

        for d in data:
            calculated = list(egcd(d[0][0], d[0][1]))
            solution = d[1]
            self.assertEqual(calculated, solution)

    def test_mod(self):
        # [[input], [output]]
        data = [[[0, 1], [0]],
                [[11, 2], [1]],
                [[-3, 25], [22]],
                [[2**10203, 101], [8]],
                [[-2**10203, 101], [93]]]

        for d in data:
            calculated = mod(d[0][0], d[0][1])
            solution = d[1][0]
            self.assertEqual(calculated, solution)


    def test_modinv(self):
        # [[input], [output]]
        data = [[[0, 1], [0]],
                [[8, 5], [2]],
                [[11, 2], [1]],
                [[-3, 25], [8]],
                [[22, 49], [29]],
                [[2**10203, 101], [38]],
                [[-2**10203, 101], [63]]]

        for d in data:
            calculated = modinv(d[0][0], d[0][1])
            solution = d[1][0]
            self.assertEqual(calculated, solution)

    def test_mmodinv(self):
        # [[input], [output]]
        data = []
        m = [[1, 4, 11], [2, 5, 9], [3, 6, 8]]
        n = [[22, 6, 15], [5, 17, 13], [1, 24, 1]]
        data.append([[m, 26], [n]])
        data.append([[n, 26], [m]])

        for d in data:
            calculated = np.array(mmodinv(d[0][0], d[0][1]))
            solution = np.array(d[1][0])
            check1 = np.sum(calculated == solution) / solution.size
            check2 = np.sum(calculated.transpose() == solution) / solution.size 
            self.assertEqual(max(check1, check2), 1.0)

if __name__ == '__main__':
    unittest.main()
