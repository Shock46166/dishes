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
    print(res)