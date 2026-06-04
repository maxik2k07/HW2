import pytest
from recipes import Ingredient
from recipes import Recipe
#Ingredient
def test_ingredient_name():
    rise = Ingredient("Рис",777,"г")
    assert rise.name=="Рис"
def test_ingredient_quantity():
    rise = Ingredient("Рис",777,"г")
    assert rise.quantity==777
def test_ingredient_unit():
    rise = Ingredient("Рис",777,"г")
    assert rise.unit=="г"
def test_str():
    rise = Ingredient("Рис", 777, "г")
    assert rise.__str__()=="Рис: 777.0 г"
def test_eq_different_quantity():
    rise = Ingredient("Рис", 777, "г")
    rise2 = Ingredient("Рис", 666, "г")
    assert rise.__eq__(rise2)
def test_eq_different_name():
    rise = Ingredient("Рис", 777, "г")
    egg = Ingredient("Яйцо", 777, "г")
    assert rise.__eq__(egg)==False
def test_eq_different_unit():
    rise = Ingredient("Рис", 777, "г")
    rise2 = Ingredient("Рис", 777, "кг")
    assert rise.__eq__(rise2)==False


#Recipe
def test_recipe_title():
    pizza = Recipe("Пицца")
    assert pizza.title=="Пицца"
def test_recipe_ingredients():
    pizza = Recipe("Пицца",[Ingredient("Мука",100,"г"),Ingredient ("Курица",200,"г")])
    assert pizza.ingredients==[Ingredient("Мука",100,"г"),Ingredient ("Курица",200,"г")]
def test_add_ingredient_default():
    pizza = Recipe("Пицца",[Ingredient("Мука",100,"г"),Ingredient ("Курица",200,"г")])
    pizza.add_ingredient(Ingredient("Томат", 300, "г"))
    assert pizza.ingredients==[Ingredient("Мука",100,"г"), Ingredient("Курица",200,"г"), Ingredient("Томат", 300, "г")]
def test_add_ingredient_existing():
    pizza = Recipe("Пицца",[Ingredient("Мука",100,"г"),Ingredient ("Курица",200,"г")])
    pizza.add_ingredient(Ingredient("Курица", 300, "г"))
    assert pizza.ingredients==[Ingredient("Мука",100,"г"), Ingredient("Курица",500,"г")]
def test_scale_return_new():
    pizza = Recipe("Пицца",[Ingredient("Мука",100,"г"),Ingredient ("Курица",200,"г")])
    pizza_new = pizza.scale(1.5)
    assert pizza_new is not pizza
def test_scale_multiplication_of_each():
    pizza = Recipe("Пицца",[Ingredient("Мука",100,"г"),Ingredient ("Курица",200,"г")])
    pizza_new = pizza.scale(1.5)
    assert pizza_new.ingredients[0].quantity==150.0
    assert pizza_new.ingredients[1].quantity==300.0
def test_scale_ratio_error():
    pizza = Recipe("Пицца", [Ingredient("Мука", 100, "г"), Ingredient("Курица", 200, "г")])
    with pytest.raises(ValueError):
        pizza.scale(-666)
def test_len():
    pizza = Recipe("Пицца",[Ingredient("Мука",100,"г"),Ingredient ("Курица",200,"г"), Ingredient("Томат", 300, "г")])
    assert pizza.__len__()==3














