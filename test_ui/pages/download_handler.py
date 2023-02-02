import glob
import os


def last_file_downloaded(path):
    list_of_files = glob.glob(os.path.join(path, '*.txt'))
    last_file = max(list_of_files, key=os.path.getctime)
    return last_file
