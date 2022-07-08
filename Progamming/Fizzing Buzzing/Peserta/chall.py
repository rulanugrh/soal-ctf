import unittest


def fizzBuzz(number):
    # your code here
    pass


class TestCase(unittest.TestCase):
    def testFizzBuzz(self):
        test1 = fizzBuzz(15)
        self.assertEqual(test1, "FizzBuzz")

    def testBuzz(self):
        test2 = fizzBuzz(5)
        self.assertEqual(test2, "Buzz")

        test3 = fizzBuzz(10)
        self.assertEqual(test3, "Buzz")

    def testFizz(self):
        test4 = fizzBuzz(3)
        self.assertEqual(test4, "Fizz")

    def testNum(self):
        test5 = fizzBuzz(1)
        self.assertEqual(test5, 1)


if __name__ == "__main__":
    unittest.main()
