import csv
import pandas as pd

def csv_merge(list_of_csv_file, output_path):
  count = 1
  l = []
  for i in list_of_csv_file:
    head, sep, tail = i.partition('.')
    head = 'csv_data'+str(count)
    head= pd.read_csv('csv/'+i)  # nrows=20
    l.append(head)
    count = count + 1
  output_data = pd.concat(l)
  output_data.to_csv('csv/'+output_path, columns=['Name', 'Midterm','Lab','Final'])

  print(output_path)

if __name__ == '__main__':
  csv_merge(['class1.csv', 'class2.csv'], 'all_students.csv')