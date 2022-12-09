from pprint import pprint


def get_cook_book():
    with open("cook_book.txt", "r", encoding="utf-8") as file:
        cook_book = {}
        for line in file:
            dish = line.strip()
            ingredients_count = int(file.readline())
            cook_book.update({dish: []})
            for i in range(ingredients_count):
                ingredients = file.readline().strip()
                ingredient_name, quantity, measure = ingredients.split(" | ")
                cook_book[dish].append({
                    "ingredient_name": ingredient_name,
                    "quantity": quantity,
                    "measure": measure})
            file.readline()
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    recipes = get_cook_book()
    dishes_dict = {}
    for dish in dishes:
        if dish in recipes:
            for ingr in recipes[dish]:
                if ingr["ingredient_name"] in dishes_dict:
                    dishes_dict[ingr["ingredient_name"]]["quantity"] += (int(ingr["quantity"]) * person_count)
                else:
                    dishes_dict.setdefault(ingr["ingredient_name"], {"quantity": (int(ingr["quantity"]) * person_count),
                                                                     "measure": ingr["measure"]})
        else:
            print("Ошибка")
    return dishes_dict


def main():
    print("a - распечатать все рецепты", "b - подобрать ингредиенты на количество персон", sep="; ")
    command = input("Введите команду: ")
    if command == "a":
        pprint(get_cook_book())
    elif command == "b":
        dish = input("Название блюд: ").split(", ")
        persons = int(input("Количество персон: "))
        pprint(get_shop_list_by_dishes(dish, persons))
    else:
        pprint("Ошибка")

main()