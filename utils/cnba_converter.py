import json


def converter_CNAB():

    with open("files/CNAB.txt", "r") as f:
        f.seek(0)
        cnba_list = f.readlines()
        json_list = list()

        for item in cnba_list:
            dictionary = {
                "type": item[0],
                "date": f"{item[1:5]}-{item[5:7]}-{item[7:9]}",
                "value": int(item[9:19])/100,
                "cpf": item[19:30],
                "card": item[30:42],
                "hour": f"{item[1:5]}-{item[5:7]}-{item[7:9]} {item[42:44]}:{item[44:46]}:{item[46:48]}",
                "store_own": item[48:62].strip(),
                "store_name": item[62:81].strip(),
            }
        json_list.append(dictionary)

    with open("files/CNAB.json", "w") as write_file:
        json.dump(json_list, write_file, indent=4, ensure_ascii=False)


def read_converted_file():
    with open("files/CNAB.json", "r", encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data