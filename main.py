from file_manager import find_files, create_directory, get_file, check_file, check_directory
from config import create_config, get_config
from indexer import index_files


def main():
    # if config file doesn't exist
    if not check_file("config.txt"):
        # create config file
        create_config()
    # get and unpack config file
    files_directory = get_config("config.txt")['files_directory']
    index_directory = get_config("config.txt")['index_directory']
    extensions = get_config("config.txt")['extensions']
    delimiter = get_config("config.txt")['delimiter']
    encoding = get_config("config.txt")['encoding']
    # if files directory doesn't exist
    if not check_directory(files_directory):
        # create files directory
        create_directory(files_directory)
    # if index directory doesn't exist
    if not check_directory(index_directory):
        # create index directory
        create_directory(index_directory)
    # if there is an existing index
    if len(find_files(index_directory, ["txt"])) > 0:
        # find all files
        files = find_files(index_directory, extensions)
        # load existing index into memory
        index = load_index(index_directory, files)
    # if there are new files to index
    if len(find_files(files_directory, extensions)) > 0:
        # find all files
        files = find_files(files_directory, extensions)
        # index files
        index_files(files_directory, index_directory, delimiter, files, encoding)
    return


if __name__ == "__main__":
    main()
