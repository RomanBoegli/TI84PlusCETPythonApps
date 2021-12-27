import unittest
from PMODARIT import bitlen, p_mod, polystr, p_mul_mod

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

    
    def test_p_mul_mod(self):
        # [[input], [output]]
        data = [[[0b0010, 0b1001, 0b10011], ['1']],
                [[0b0111, 0b1110, 0b10011], ['x^3 + x^2']],
                [[0b1111, 0b1111, 0b10011], ['x^3 + x']]]

        for d in data:
            calculated = p_mul_mod(d[0][0], d[0][1], d[0][2])
            solution = d[1][0]
            self.assertEqual(calculated, solution)

if __name__ == '__main__':
    unittest.main()
