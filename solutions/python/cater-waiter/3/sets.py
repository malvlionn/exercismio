"""Functions for compiling dishes and ingredients for a catering company."""

from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)

def clean_ingredients(dish_name, dish_ingredients):
    return (dish_name, set(dish_ingredients))

def check_drinks(drink_name, drink_ingredients):
    if len(ALCOHOLS & set(drink_ingredients)) > 0:
        return drink_name + " Cocktail"
    return drink_name + " Mocktail"

def categorize_dish(dish_name, dish_ingredients):
    """hi"""
    if dish_ingredients <= VEGAN:
        jenis = "VEGAN"
    elif dish_ingredients <= VEGETARIAN:
        jenis = "VEGETARIAN"
    elif dish_ingredients <= KETO:
        jenis = "KETO"
    elif dish_ingredients <= PALEO:
        jenis = "PALEO"
    elif dish_ingredients <= OMNIVORE:
        jenis = "OMNIVORE"
    return dish_name + f": {jenis}"

def tag_special_ingredients(dish):
    return (dish[0], (SPECIAL_INGREDIENTS & set(dish[1])))

def compile_ingredients(dishes):
    kocak = set()
    for isi in dishes:
        kocak |= isi
    return kocak
    
def separate_appetizers(dishes, appetizers):
    return list((set(dishes) - set(appetizers)))

def singleton_ingredients(dishes, intersection):
    all_singletons = set()
    for dish in dishes:
        all_singletons |= dish
    all_singletons -= intersection
    
    return all_singletons