import os
import time
import string
import random


class FileWriter:
    def __init__(self, data):
        self.data = data

    def write_to_file(self):
        # Create the output directory if it doesn't exist
        os.makedirs("output", exist_ok=True)

        # Generate a unique character for the filename
        unique_char = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=1))

        # Get the current time
        current_time = time.strftime("%Y%m%d%H%M%S")

        # Generate the filename
        filename = f"output/{current_time}_{unique_char}.txt"

        # Open the file in write mode and write each element of the data array
        with open(filename, 'w') as file:
            for element in self.data:
                file.write(str(element) + '\n')

        print(f"Data written to file: {filename}")


# Example usage:
def value_pars(data):
    file_writer = FileWriter(data)
    file_writer.write_to_file()


