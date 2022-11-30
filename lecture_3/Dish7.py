class Dish7:
    MAX_INGREDIENTS = 7

    def __init__(self, name, is_vegetarian, ingredients=[]):
        self.name = name
        self.is_vegetarian = is_vegetarian
        self.ingredients = []
        for ingredient in ingredients:
            self.add_ingredient(ingredient)

    def can_add_ingredient(self, ingredient):
        """Return True if we should allow to add another ingredient."""
        return len(self.ingredients) < self.MAX_INGREDIENTS and ingredient not in self.ingredients

    def add_ingredient(self, ingredient):
        """Add an ingredient to the dish."""
        if not self.can_add_ingredient(ingredient):
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


if __name__ == '__main__':
    d = Dish7("H", True, ["1", "2", "3"])
    print(d.ingredients)
    d.add_ingredient("4")
    print(d.ingredients)
    d.add_ingredient("4")   # can't because 4 already exist
    print(d.ingredients)
    d.add_ingredient("5")
    print(d.ingredients)
    d.add_ingredient("6")
    print(d.ingredients)
    d.add_ingredient("7")
    print(d.ingredients)
    d.add_ingredient("8")   # can't because there are already 7 ingredients
    print(d.ingredients)