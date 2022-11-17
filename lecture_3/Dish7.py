class Dish7:
    MAX_INGREDIENTS = 7

    def __init__(self, name, is_vegetarian, ingredients=[]):
        self.name = name
        self.is_vegetarian = is_vegetarian
        self.ingredients = ingredients
        for ingredient in ingredients:
            self.add_ingredient(ingredient)

    def can_add_ingredient(self):
        """Return True if we should allow to add another ingredient."""
        return len(self.ingredients) < self.MAX_INGREDIENTS

    def add_ingredient(self, ingredient):
        """Add an ingredient to the dish."""
        if not self.can_add_ingredient():
            return False
        self.ingredients.append(ingredient)
        return True

    def remove_ingredient(self, ingredient):
        """Remove an ingredient from the dish."""
        self.ingredients.remove(ingredient)

    def get_total_calories(self):
        """Calculate calories based on the list of the ingredients."""
        calories = 0
        for ingredient in self.ingredients:
            calories = calories + ingredient.calculate_calories()
        return calories

    def __str__(self):
        calories = self.get_total_calories()
        return f"{self.name} has {calories} calories in it."