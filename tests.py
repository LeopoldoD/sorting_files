import unittest
from unittest.mock import patch
import io
import unittest.mock
import warnings
import sorting_files.sort_files as sorting
from sorting_files.sort_files import FileSorter

mock_stdout = unittest.mock.patch('sys.stdout', new_callable=io.StringIO)


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.sorting_files = sorting
        self.sorter = FileSorter()

    def test_get_list_of_files(self):
        self.assertEqual(self.sorting_files.get_list_of_files("files"),
        ['file2.txt',
         'file3.txt',
         'file1.txt',
         'file4.txt',
         'file5.txt',
         'file7.txt',
         'file6.txt',
         'file10.txt',
         'file8.txt',
         'file9.txt'])

    def test_create_directory(self):
        self.assertTrue(self.sorting_files.create_directory('temp'), True)

    def test_clean_directory(self):
        self.assertTrue(self.sorting_files.clean_directory('temp'), True)

    def test_get_source_directory(self):
        self.assertEqual(self.sorter.get_source_directory(), "files/")

    def test_get_temp_directory(self):
        self.assertEqual(self.sorter.get_temp_directory(), "temp/")

    def test_get_buffer_size(self):
        self.assertEqual(self.sorter.get_buffer_size(), 10)

    def test_split_files(self):
        self.assertTrue(self.sorter.split_files(), True)

    def test_get_min_hap(self):
        warnings.simplefilter('ignore', ResourceWarning)
        self.assertEqual(len(self.sorter.get_min_heap()), 12)

    @mock_stdout
    def test_min_heap_sort(self, stdout):
        self.sorter.min_heap_sort()
        value = stdout.getvalue()
        self.assertEqual(value, '0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,4,5,6,6,7,8,8,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,11,11,11,11,11,12,14,16,18,20,44,44,44,44,44,44,44,100,1000,10000,100000,')

if __name__ == '__main__':
    unittest.main()