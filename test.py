import unittest
import testing_intro


class TestMain(unittest.TestCase):
    def setUp(self):
        print('About to test a function')  # prints this before every test

    def test_do_stuff(self):
        test_param = 10
        result = testing_intro.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'sfjhfdj'
        result = testing_intro.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)  # checks if the result give ValueErr

    def test_do_stuff3(self):
        test_param = None
        result = testing_intro.do_stuff(test_param)
        self.assertEqual(result, 'please enter a number')

    def tearDown(self):
        print('cleaning up')  # prints this at the end of this function


if __name__ == '__main__':
    unittest.main()
