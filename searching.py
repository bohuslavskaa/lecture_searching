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
        data = json.load(file_obj)
        if field in data.keys():
            return data[field]
        else:
            return None

def linear_search(sekvence, cislo):
    slovnik = {"positions": [], "count": 0}
    for idx, i in enumerate(sekvence):
        if i == cislo:
            slovnik["positions"].append(idx)
            slovnik["count"] += 1
    return slovnik
def main():
    file_name = 'sequential.json'
    seq = read_data(file_name, 'unordered_numbers')
    dictt = linear_search(seq,0)
    print(dictt)

if __name__ == '__main__':
    main()