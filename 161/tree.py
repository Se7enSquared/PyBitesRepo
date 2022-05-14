import os


def count_dirs_and_files(directory='.'):
    """Count the amount of of directories and files in passed in "directory" arg.
        Return a tuple of (number_of_directories, number_of_files)
    """
    dir_list = []
    file_list = []
    for root, dirs, files in os.walk(directory):
        for dir in dirs:
            dir_list.append(dir)
        for file in files:
            file_list.append(file)
    return (len(dir_list), len(file_list))
