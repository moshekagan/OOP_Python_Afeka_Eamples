class Ingredient:
    HEALTHY_CALORIES_UPPER_BOUND = 100

    def __init__(self, name, carbs, fats, proteins):
        self.name = name
        self.carbs = carbs
        self.fats = fats
        self.proteins = proteins

    def calculate_calories(self):
        return (self.carbs * 4
            + self.fats * 9
            + self.proteins * 4)

    def is_healthy(self):
        return self.calculate_calories() < self.HEALTHY_CALORIES_UPPER_BOUND


"""
# ---- EXAMPLES CODE:

banana = Ingredient('Banana', carbs=23, fats=0.3, proteins=1.1)
melon = Ingredient('Melon', carbs=8, fats=0.2, proteins=0.8)

# all instances have access the value of "HEALTHY_CALORIES_UPPER_BOUND"
print(banana.HEALTHY_CALORIES_UPPER_BOUND)
print(melon.HEALTHY_CALORIES_UPPER_BOUND)

print(f"Is Banana healthy? -- {banana.is_healthy()}")
print(f"Is Melon healthy? -- {melon.is_healthy()}")

# Direct access from the Class to global variable
print(Ingredient.HEALTHY_CALORIES_UPPER_BOUND)  # 100

# Also can change the value
Ingredient.HEALTHY_CALORIES_UPPER_BOUND = 200
print(Ingredient.HEALTHY_CALORIES_UPPER_BOUND)  # 200


# This will not work!
print(Ingredient.name)
Ingredient.is_healthy()

melon = Ingredient('Melon', carbs=8, fats=0.2, proteins=0.8)
# melon is an Instance of Ingredient and can call with self!
melon.is_healthy()


"""