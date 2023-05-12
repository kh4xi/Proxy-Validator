import os
from pathlib import Path


class FileWriter:
    def __init__(self, directory):
        self.directory = directory

    def write_file(self, filename, array):
        try:
            file_path = os.path.join(self.directory, filename)
            with open(file_path, 'w') as file:
                for item in array:
                    file.write(str(item) + '\n')
            print(f"File '{filename}' has been written to {self.directory}.")
        except Exception as e:
            print(f"An error occurred while writing the file: {e}")


# Example usage
def make_output(long_path, filename, data):
    desktop_path = Path.home() / long_path
    file_writer = FileWriter(desktop_path)
    file_writer.write_file(filename, data)


