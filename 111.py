with open(r'C:\\Users\\Веста\\Desktop\\ЦоЦ\\JO\\venv\\recipes.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dishes = line.strip()
        meal_count = file.readline()
        meal_list = []
        for i in range(int(meal_count)):
            num = file.readline().strip()
            ingredient_name, quantity, measure = num.split(' | ')
            meal_list.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })
        file.readline()
        cook_book[dishes] = meal_list
    print('cook_book =', cook_book)