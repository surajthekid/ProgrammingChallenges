csv_combiner = __import__("csv-combiner") # importing file like this since filename has '-'
import unittest


class Test(unittest.TestCase):
    def test0_valid_csv(self):
        # test valid file
        valid_name = './fixtures/real.csv'
        valid = csv_combiner.is_csv_file(valid_name)
        self.assertTrue(valid)
        # test invalid file
        invalid_name = './fixtures/not.cs'
        invalid = csv_combiner.is_csv_file(invalid_name)
        self.assertFalse(invalid)

    def test1_getfile(self):
        # test if parse successfully path to file
        filename = './fixtures/real.csv'
        filename = csv_combiner.get_filename(filename)
        expected = 'real.csv'
        self.assertEqual(filename, expected)

        filename = './fixtures/real2.csv'
        filename = csv_combiner.get_filename(filename)
        expected = 'real2.csv'
        self.assertEqual(filename, expected)

    def test2_escape(self):
        # test escape cases from reading
        # escape chars should be preserved
        test_str = "\"Gingham\" Shorts"
        test_str = csv_combiner.escape_quotes(test_str)
        expected = "\"Gingham\" Shorts"
        self.assertEqual(test_str, expected)

    def test3_removedq(self):
        # remove case of double quotes at end of string
        test_str = "test\""
        test_str = csv_combiner.remove_dq(test_str)
        expected = "test"
        self.assertEqual(test_str, expected)
        
        # remove case of a pair of double quotes in string
        test_str = "test\"\"test"
        test_str = csv_combiner.remove_dq(test_str)
        expected = "test\"test"
        self.assertTrue(test_str, expected)





if __name__ == '__main__':
    unittest.main()
