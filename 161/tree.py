import os


def count_dirs_and_files(directory='.'):
    """Count the amount of of directories and files in passed in "directory" arg.
        Return a tuple of (number_of_directories, number_of_files)
    """
    dir_list = []
    file_list = []
    for root, dirs, files in os.walk(directory):
        dir_list.extend(iter(dirs))
        file_list.extend(iter(files))
    return (len(dir_list), len(file_list))
