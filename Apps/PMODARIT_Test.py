import unittest
from PMODARIT import bitlen, p_mod, polystr

class PMODARIT_Test(unittest.TestCase): #creating the class
    

    def test_bitlen(self):
        data = [1, 2, -5, 10, -50, 100, 1000, 2**10, 2**10**2]
        for d in data:
            calculated = bitlen(d)
            solution = d.bit_length()
            self.assertEqual(calculated, solution)

    def test_p_mod(self):
        # [[input], [output]]
        data = [[[0b100000, 0b110011], ['x^4 + x + 1']],
                [[0b10011, 0b110011], ['x^4 + x + 1']],
                [[0b110011, 0b10011], ['x^2 + x']]]

        for d in data:
            calculated = polystr(p_mod(d[0][0], d[0][1]))
            solution = d[1][0]
            self.assertEqual(calculated, solution)

if __name__ == '__main__':
    unittest.main()
