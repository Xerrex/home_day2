import unittest

from issAPI import iss_info

class issAPITests(unittest.TestCase):

    def test_fail_with_params(self):
        pass

    def test_returns_dictionary(self):
        e_value = dict()
        r_value =iss_info()

