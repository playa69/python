import json
import re
#кодировка?
periodic_table = json.load(open('periodic_table.json', encoding='utf-8'))

with open("output_file_3.txt", "w") as new_file:
    with open("import_file_3.txt", "r") as file:
        data = file.read()
        pattern ='[A-Z]{1}[a-z]{0,2}'
        chemical= re.findall(pattern, data)
        for i in range(len(chemical)):
            new_file.write(periodic_table.get(chemical[i]))
file.close()
new_file.close()



import json
import re
 
 
def read_periodic_mapping(json_path: str) -> dict
    with open(json_path, 'r') as file:
        return json.load(file)
 
 
def read_file(file_path: str) -> str:
    with open(file_path, 'r') as file:
        return file.read()
 
 
def get_result_string(json_path: str, file_path: str) -> str:
    periodic_mapping = read_periodic_mapping(json_path)
    elements_string = read_file(file_path)
 
    elements = re.split('(?=[A-Z])', elements_string)
 
    return ''.join(
        map(lambda x: periodic_mapping.get(x, ''), elements)
    )
 
 
if __name__ == "__main__":
    print(get_result_string('periodic_table.json', 'import_file_3.txt'))