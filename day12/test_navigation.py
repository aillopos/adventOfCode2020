import unittest
import navigation


class TestSum(unittest.TestCase):
    def test_get_total_instruction_ferry(self):
        instructions = navigation.read_input("test_data.txt")
        expect = 24
        self.assertEqual(expect, navigation.get_total_instruction_ferry(instructions),
                         "total no of fields should be: {}".format(expect))

    def test_get_total_instruction_waypoint(self):
        instructions = navigation.read_input("test_data.txt")
        expect = 286
        self.assertEqual(expect, navigation.get_total_instruction_waypoint(instructions),
                         "total no of fields should be: {}".format(expect))
