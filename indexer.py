from re import sub
from file_manager import get_file, check_file, create_index_file, append_index_file


def index_files(files_directory, index_directory, delimiter, files, encoding):
    # for every file in files
    for file in files:
        # open file and get text
        text = get_file(files_directory, file, encoding)
        # split text by delimiter
        text = text.split(delimiter)
        # for every word in text
        for word in text:
            # sanitise word
            word = sub(r'\W+', '', word).lower()
            # check word has required length
            if len(word) > 2:
                # if word file doesn't exist
                if not check_file("{0}/{1}.txt".format(index_directory, word)):
                    # create json object as string
                    file_data = "{{\"{0}\": [{{\"file_name\": \"{1}\", \"occurrences\": 1}}]}}".format(word, file)
                    # create word file and write data
                    create_index_file(index_directory, word, file_data, encoding)
                else:
                    # otherwise append data
                    append_index_file(index_directory, word, file, encoding)
    return 1
