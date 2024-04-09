import unittest
import math
import integration
from integration import trapezoidal_integration

class integration_unittests(unittest.TestCase):

    def test_sin(self):
        def f(x):
            return math.sin(x)
        self.assertAlmostEqual(trapezoidal_integration(0, math.pi, f , 10000), 2, places=2)

    def test_exp(self):
        def f(x):
            return math.exp(x)
        self.assertAlmostEqual(trapezoidal_integration(1, 2, f, 9000), 4.6708, places=2)

    def test_polynomial(self):
        def f(x):
            return 2*(x**3)+9*(x**2)-3
        self.assertAlmostEqual(trapezoidal_integration(7, 8, f, 12000), 1351.5, places=2)

if __name__ == '__main__':
    unittest.main()