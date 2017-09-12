from unittest import TestCase
import numpy as np

points = np.genfromtxt("./data/data.csv", delimiter=",")
learning_rate = 0.0001
initial_b = 2
initial_m = 6
num_iterations = 15

class TestError_calculator(TestCase):
    def test_error_calculator(self):
        from build import error_calculator
        error = error_calculator(initial_b, initial_m, points)
        self.assertAlmostEqual(error, 51903.5527927)

    def test_gradient_descent(self):
        from build import error_calculator, gradient_descent
        error_before = error_calculator(initial_b, initial_m, points)
        b, theta, error = gradient_descent(initial_b, initial_m, points, learning_rate, num_iterations)
        error_after = error_calculator(b[-1], theta[-1], points)
        self.assertGreater(error_before, error_after)