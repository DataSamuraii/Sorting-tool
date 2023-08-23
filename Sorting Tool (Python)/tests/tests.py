import unittest
from ..task.main import process_num, get_input, output_natural, output_by_count
from collections import Counter
from io import StringIO


class TestMainFunctions(unittest.TestCase):

    def test_process_num(self):
        self.assertEqual(process_num('5'), 5)
        self.assertEqual(process_num('100'), 100)
        self.assertIsNone(process_num('not_a_number'))

    def test_get_input(self):
        self.assertEqual(get_input('word', StringIO('hello world')), ['hello', 'world'])
        self.assertEqual(get_input('line', StringIO('hello world')), ['hello world'])
        self.assertEqual(get_input('long', StringIO('42 43')), ['42', '43'])

    def test_output_natural(self):
        output = StringIO()
        output_natural([1, 2, 3], 'word', output)
        self.assertEqual(output.getvalue(), 'Total words: 3\nSorted data:1 2 3\n')

    def test_output_by_count(self):
        output = StringIO()
        counted_input_list = sorted(Counter([1, 2, 2, 3, 3, 3]).items())
        output_by_count(counted_input_list, 'number', output)
        expected_output = (
            'Total numbers: 6.\n'
            '1: 1 time(s), 16%.\n'
            '2: 2 time(s), 33%.\n'
            '3: 3 time(s), 50%.\n'
        )
        self.assertEqual(output.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
