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
        pass

    def test2_escape(self):
        pass

    def test3_removedq(self):
        pass

    def test4_parse(self):
        pass




if __name__ == '__main__':
    unittest.main()
