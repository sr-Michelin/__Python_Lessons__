import unittest
import sys

sys.path.append('E:\\DOCK\\Python_M\\vеnv\\+LESSONS\\+BASE+\\UNITTEST\\I')
from tested_sample import get_fd_nm


class testing(unittest.TestCase):
    '''Testing the get_fd_nm and outhers modules (in the future)'''

    def test_first_name(self):
        formatted_name = get_fd_nm('mike')
        self.assertEqual(formatted_name, 'Mike')

    def test_first_last_name(self):
        formatted_name = get_fd_nm('mike', 'shevchenko')
        self.assertEqual(formatted_name, 'Mike Shevchenko')

    def test_first_middle_last_name(self):
        formatted_name = get_fd_nm('mike', 'shevchenko', 'sergiyovich')
        self.assertEqual(formatted_name, 'Mike Sergiyovich Shevchenko')


if __name__ == '__main__':
    unittest.main()
