import unittest


def sum_of_intervals(intervals):
    output = set()
    for start, stop in intervals:
        for i in range(start, stop):
            output.add(i)

    return len(output)


class TestStuff(unittest.TestCase):
    def test_stuff(self):
        self.assertEqual(sum_of_intervals([(1, 5)]), 4)
        self.assertEqual(sum_of_intervals([(1, 5), (6, 10)]), 8)
        self.assertEqual(sum_of_intervals([(1, 5), (1, 5)]), 4)
        self.assertEqual(sum_of_intervals([(1, 4), (7, 10), (3, 5)]), 7)


if __name__ == '__main__':
    unittest.main()
