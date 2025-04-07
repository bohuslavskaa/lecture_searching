import json
import os
# get current working directory path
cwd_path = os.getcwd()

def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r") as file_obj:
        data = json.load(file_obj)[field]
    return data

def main():
    file_name = 'sequential.json'
    seq = read_data(file_name, 'unordered_numbers')
    print(seq)
    pass

if __name__ == '__main__':
    main()