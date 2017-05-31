from json import loads, dumps
from os import path, listdir, makedirs


def find_files(directory, extensions):
    # initialise files list
    files = []
    # for every file found in directory
    for file in listdir(directory):
        # check file has correct extension
        if file.split(".")[1] in extensions:
            # append file to files list
            files.append(file)
    # return list of files
    return files


def get_file(files_directory, file, encoding):
    # open file
    with open("{0}/{1}".format(files_directory, file), "r", encoding=encoding) as data:
        # return file data
        return data.read()


def create_index_file(index_directory, word, file_data, encoding):
    # create file and open
    with open("{0}/{1}.txt".format(index_directory, word), "w+", encoding=encoding) as data:
        # write data to file
        data.write(file_data)
    return


def append_index_file(index_directory, word, file_data, encoding):
    # open existing index file
    with open("{0}/{1}.txt".format(index_directory, word), "r+", encoding=encoding) as data:
        # load json string into object
        word_object = loads(data.read())
        # for every file associated with word
        for file in word_object[word]:
            # if the file is already associated with the word
            if file['file_name'] == file_data:
                # increment its occurrences by 1
                file['occurrences'] +=1
                # dump the object into json string
                word_object = dumps(word_object)
                # go to beginning of file
                data.seek(0)
                # overwrite existing data
                data.write(word_object)
                return
        # set file data to new object
        file_data = {"file_name": file_data, "occurrences": 1}
        # append the new file data to the existing word object
        word_object[word].append(file_data)
        # dump the object into json string
        word_object = dumps(word_object)
        # go to beginning of file
        data.seek(0)
        # overwrite existing data
        data.write(word_object)
    return


def create_directory(directory):
    # create directory
    makedirs(directory)
    # return success
    return 1


def check_directory(directory):
    # if directory exists
    if path.isdir(directory):
        # return success
        return 1
    # otherwise return nothing
    return


def check_file(file):
    # if file exists
    if path.exists(file):
        # return success
        return 1
    # otherwise return nothing
    return
