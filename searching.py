import os
import json
# get current working directory path
cwd_path = os.getcwd()

with open("sequential.json") as data_file:
    data = json.load(data_file)

def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path) as data_file:
        data = json.load(data_file)
    return  data[field]



def main():
    file_name = 'sequential.json'
    seq = read_data(file_name, 'unordered_numbers')
    print(seq)
    pass


if __name__ == '__main__':
    main()