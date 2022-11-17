class Dish:
    def __init__(self, name, is_vegetarian, ingredients):
        self.name = name
        self.is_vegetarian = is_vegetarian
        self.ingredients = ingredients

    def get_total_calories(self):
        """Calculate calories based on the list of the ingredients."""
        calories = 0
        for ingredient in self.ingredients:
            calories = calories + ingredient.calculate_calories()
        return calories

    def __str__(self):
        calories = self.get_total_calories()
        return f"{self.name} has {calories} calories in it."
