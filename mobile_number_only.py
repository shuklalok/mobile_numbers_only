# AUTHOR: Alok Shukla
# E-MAIL: 20066073+shuklalok@users.noreply.github.com
"""
Single script for extracting only Indian mobile numbers
from input provided as CSV files with only 2 columns -
First contact name information and second contact information.
The contact information MUST be a single entry of  a Toll Free,
Land Line or a Mobile number (All Indians).
"""
import os
from os import listdir
import csv

TOLL_FREE = '18'
LAND_LINE_SPACE = 2
CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIRECTORY = os.path.join(CURRENT_DIRECTORY, "output")
if not os.path.exists(OUTPUT_DIRECTORY):
    os.mkdir(OUTPUT_DIRECTORY)


def read_write_file(filename):
    """
    Reads the input file from CURRENT_DIRECTORY,
    Removes 'No Contact', 'Toll Free' and 'Land Line' numbers,
    Writes the output file in OUTPUT_DIRECTORY.
    :param filename: Name of the input file
    :type str
    :return: Nothing
    :rtype: None
    """
    current_file = os.path.join(CURRENT_DIRECTORY, filename)
    output_file = os.path.join(OUTPUT_DIRECTORY, filename)
    with open(current_file, encoding="utf8", mode="r") as csv_file, open(
        output_file, encoding="utf8", mode="w", newline='\n'
    ) as csv_out:
        csv_reader = csv.reader(csv_file, delimiter=",")
        csv_writer = csv.writer(
            csv_out, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL
        )
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                # Ignore 'No Contact', 'Toll Free' and 'Land Line' numbers,
                if row[1] != "" and row[1].count(" ") < LAND_LINE_SPACE and not row[1].startswith(TOLL_FREE):
                    name = row[0] if row[0] != "" else "No_Name"
                    mobile = str(int(row[-1].replace(" ", "")))
                    output_data = name + ":" + mobile
                    csv_writer.writerow(output_data.split(":"))
            line_count += 1
    print("Total lines parsed from %s: %s" % (current_file, line_count))


def find_csv_filenames(path_to_dir, suffix=".csv"):
    """
    Gets the list of all files with provided extension.
    CSV extension by default.
    :param path_to_dir: The directory where the input files are present
    :type path_to_dir: str
    :param suffix: Input files extension
    :type suffix: str
    :return: List of files with given extension.
    :rtype: list
    """
    file_names = listdir(path_to_dir)
    return [fn for fn in file_names if fn.endswith(suffix)]


if __name__ == '__main__':
    try:
        for file_name in find_csv_filenames(os.getcwd()):
            read_write_file(file_name)
        print("Output Files are saved in: %s" % OUTPUT_DIRECTORY)
    except Exception as e:
        print("An exception occurred", e)
