import unittest

import seats


class TestSum(unittest.TestCase):
    seat_plan = [['L', '.', 'L', 'L', '.', 'L', 'L', '.', 'L', 'L'],
                 ['L', 'L', 'L', 'L', 'L', 'L', 'L', '.', 'L', 'L'],
                 ['L', '.', 'L', '.', 'L', '.', '.', 'L', '.', '.'],
                 ['L', 'L', 'L', 'L', '.', 'L', 'L', '.', 'L', 'L'],
                 ['L', '.', 'L', 'L', '.', 'L', 'L', '.', 'L', 'L'],
                 ['L', '.', 'L', 'L', 'L', 'L', 'L', '.', 'L', 'L'],
                 ['.', '.', 'L', '.', 'L', '.', '.', '.', '.', '.'],
                 ['L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L'],
                 ['L', '.', 'L', 'L', 'L', 'L', 'L', 'L', '.', 'L'],
                 ['L', '.', 'L', 'L', 'L', 'L', 'L', '.', 'L', 'L']]

    def test_reach_equilibrium_I(self):
        result = seats.reach_equilibrium(self.seat_plan, seats.get_neighbor_seats, 4)
        expected = 37
        self.assertEqual(expected, result, "part I: number of occupied seats should be {}".format(expected))

    def test_reach_equilibrium_II(self):
        result = seats.reach_equilibrium(self.seat_plan, seats.get_visible_seats, 5)
        expected = 26
        self.assertEqual(expected, result, "part II: number of occupied seats should be {}".format(expected))

    def test_get_first_seat_along_axis(self):
        seat_line = ["L", ".", "L", "#"]
        result = seats.get_first_seat_along_axis(seat_line, 2, 4, 1)
        self.assertEqual("#", result, "should return '#'")
        result = seats.get_first_seat_along_axis(seat_line, 2, 4, -1)
        self.assertEqual("L", result, "should return 'L'")

    def test_get_visible_seats(self):
        result = seats.get_visible_seats(self.seat_plan, 3, 3,
                                         {seats.rows: len(self.seat_plan), seats.cols: len(self.seat_plan[0])})
        expected = ["L" for _ in range(8)]
        self.assertEqual(expected, result, "part II: neighbors should be {}".format(expected))

        seat_plan = [['.', '.', '.', '.', '.', '.', '.', '#', '.'], ['.', '.', '.', '#', '.', '.', '.', '.', '.'],
                     ['.', '#', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
                     ['.', '.', '#', 'L', '.', '.', '.', '.', '#'], ['.', '.', '.', '.', '#', '.', '.', '.', '.'],
                     ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['#', '.', '.', '.', '.', '.', '.', '.', '.'],
                     ['.', '.', '.', '#', '.', '.', '.', '.', '.']]
        result = seats.get_visible_seats(seat_plan, 4, 3,
                                         {seats.rows: len(seat_plan), seats.cols: len(seat_plan[0])})
        expected = 8
        self.assertEqual(expected, result.count(seats.occupied), "part II: neighbors should be {}".format(expected))

        seat_plan = [['.', '#', '#', '.', '#', '#', '.'], ['#', '.', '#', '.', '#', '.', '#'],
                     ['#', '#', '.', '.', '.', '#', '#'], ['.', '.', '.', 'L', '.', '.', '.'],
                     ['#', '#', '.', '.', '.', '#', '#'], ['#', '.', '#', '.', '#', '.', '#'],
                     ['.', '#', '#', '.', '#', '#', '.']]
        result = seats.get_visible_seats(seat_plan, 3, 3,
                                         {seats.rows: len(seat_plan), seats.cols: len(seat_plan[0])})
        expected = 0
        self.assertEqual(expected, result.count(seats.occupied), "part II: neighbors should be {}".format(expected))


if __name__ == '__main__':
    unittest.main()
