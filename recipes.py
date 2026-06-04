class Ingredient:
    def __init__(self, name: str, quantity: float, unit: str) -> None:
        self.name = name
        self.quantity = quantity
        self.unit = unit

    @property
    def quantity(self) -> float:
        return self._quantity

    @quantity.setter
    def quantity(self, value) -> None:
        if value <= 0:
            raise ValueError("Количество должно быть положительным")
        self._quantity = float(value)

    def __str__(self) -> str:
        return f"{self.name}: {self._quantity} {self.unit}"

    def __repr__(self) -> str:
        return f"Ingredient('{self.name}', {self._quantity}, '{self.unit}')"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Ingredient):
            return NotImplemented
        return self.name == other.name and self.unit == other.unit


class Recipe:
    def __init__(self, title: str, ingredients: list = None) -> None:
        self.title = title
        self.ingredients = ingredients if ingredients is not None else []

    def add_ingredient(self, ingredient: Ingredient) -> None:
        for existing in self.ingredients:
            if existing == ingredient:
                existing.quantity += ingredient.quantity
                return
        self.ingredients.append(Ingredient(ingredient.name, ingredient.quantity, ingredient.unit))

    @staticmethod
    def is_valid_ratio(ratio) -> bool:
        return (isinstance(ratio, int) or isinstance(ratio, float)) and ratio > 0

    def scale(self, ratio: float):
        if not Recipe.is_valid_ratio(ratio):
            raise ValueError("Коэффициент должен быть положительным числом")
        scaled = Recipe(self.title)
        for ingredient in self.ingredients:
            scaled.ingredients.append(Ingredient(ingredient.name, ingredient.quantity * ratio, ingredient.unit))
        return scaled

    def __len__(self) -> int:
        return len(self.ingredients)

    def __str__(self) -> str:
        lines = [self.title]
        for ingredient in self.ingredients:
            lines.append(f"- {ingredient}")
        return "\n".join(lines)


class DietaryRecipe(Recipe):
    def __init__(self, title: str, diet_type: str, ingredients: list = None) -> None:
        super().__init__(title, ingredients)
        self.diet_type = diet_type

    def scale(self, ratio: float):
        scaled_recipe = super().scale(ratio)
        return DietaryRecipe(scaled_recipe.title, self.diet_type, scaled_recipe.ingredients)

    def __str__(self) -> str:
        return f"[{self.diet_type}] {super().__str__()}"
