"""from <file_path> import <class_name>"""
from lecture_3.Dish import Dish
from lecture_3.Ingredient import Ingredient

"""Usually file name will be same as the class name, buy not always"""

ingredients = [
    Ingredient('Butter', carbs=0.1, fats=81.9, proteins=0.9),
    Ingredient('Honey', carbs=82, fats=0, proteins=0.3),
    Ingredient('Flour', carbs=79, fats=1.8, proteins=7),
]
bread = Dish("Lembas Bread", is_vegetarian=True, ingredients=ingredients)
print(bread)    #Lembas Bread has 1430.5 calories in it.
