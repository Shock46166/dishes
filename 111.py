## Задача 1
import json
with open(r'C:\\Users\\Веста\\Desktop\\ЦоЦ\\JO\\venv\\recipes.txt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dishes = line.strip()
        meal_count = int(file.readline())
        meal_list = []
        for i in range(meal_count):
            num = file.readline().strip()
            ingredient_name, quantity, measure = num.split(' | ')
            meal_list.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })
        file.readline()
        cook_book[line.strip()] = meal_list
    res = json.dumps(cook_book, indent=2, ensure_ascii=False)
    # print(res)

## Задача 2
def get_shop_list_by_dishes(person_count: int, dishes: list):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for consist in cook_book[dish]:
                if consist['ingredient_name'] in result:
                    result[consist['ingredient_name']]['quantity'] += consist['quantity'] * person_count
                else:
                    result[consist['ingredient_name']] = {'measure': consist['measure'],'quantity': (consist['quantity'] * person_count)}
        else:
            print('Такого блюда нет в книге')
    # print(result)
get_shop_list_by_dishes(2, ['Запеченный картофель', 'Омлет'])

## Задача 3
import os

path_to_folder = r"C:\Users\Веста\Desktop\ЦоЦ\JO\venv"
directory = os.listdir(path_to_folder)

file_list = []
for file in directory:
    with open(os.path.join(path_to_folder, file), encoding='utf-8') as f:
        file_list.append(f.readlines())

id = 0
for list in file_list:
    list.insert(0, len(list))
    list.insert(0, directory[id])
    id += 1

sorted_file_list = file_list.sort(key=lambda x: len(x))

with open('result.txt', 'w', encoding='utf-8') as result_file:
    result_file.write(file_list[0][0] + '\n' + str(file_list[0][1]) + '\n' + ''.join(file_list[0][2:]) + '\n')
    result_file.write(file_list[1][0] + '\n' + str(file_list[1][1]) + '\n' + ''.join(file_list[1][2:]) + '\n')
    result_file.write(file_list[2][0] + '\n' + str(file_list[2][1]) + '\n' + ''.join(file_list[2][2:]) + '\n')
