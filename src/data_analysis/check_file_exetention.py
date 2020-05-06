import os
from zipfile import ZipFile

def zip_files(search_directory, selected_extensions, output_path):
  with ZipFile(output_path, 'w') as zipObj2:
    for file in os.listdir(search_directory):
      if file.endswith(tuple(selected_extensions)):
        print(type(os.path.join(search_directory, file)))
        # Create a ZipFile Object
        zipObj2.write(os.path.join(search_directory, file))

if __name__ == '__main__':
  zip_files('csv', ['.jpg', '.csv'], 'my_stuff.zip')