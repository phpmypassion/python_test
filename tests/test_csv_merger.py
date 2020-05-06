import unittest
from data_analysis import csv_merger

class MyTestCase(unittest.TestCase):
  def test_arguments(self):
    all_students = csv_merger.csv_merge(['class1.csv', 'class2.csv'], 'all_students.csv')
    self.assertEqual(all_students, 'all_students.csv')


if __name__ == '__main__':
  unittest.main()
