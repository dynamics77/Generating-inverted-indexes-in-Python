from json import loads


def create_config():
    # create config file
    with open("config.txt", "w+") as config:
        # write default values
        config.write("{\n"
                     "  \"files_directory\": \"files\",\n"
                     "  \"index_directory\": \"index\",\n"
                     "  \"extensions\": [\"txt\"],\n"
                     "  \"delimiter\": \" \",\n"
                     "  \"encoding\": \"UTF-8\"\n"
                     "}\n")
        # return success
        return 1


def get_config(file):
    # open file
    with open(file, "rb") as data:
        # set data to value of file
        data = loads(data.read())
        # return data
        return data
