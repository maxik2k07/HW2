import pytest
from recipes import Ingredient
from recipes import Recipe
from recipes import ShoppingList

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
        pizza.scale(-666.0)
def test_len():
    pizza = Recipe("Пицца",[Ingredient("Мука",100,"г"),Ingredient ("Курица",200,"г"), Ingredient("Томат", 300, "г")])
    assert pizza.__len__()==3


#ShoppingList
def test_add_recipe_works():
    first_list = ShoppingList()
    first_list.add_recipe(Recipe("Пицца",[Ingredient("Мука",100,"г"),Ingredient ("Курица",200,"г"), Ingredient("Томат", 300, "г")]),3.0)
    assert len(first_list._items)==3
    assert first_list._items[0][1]=="Пицца"
def test_add_recipe_error():
    first_list = ShoppingList()
    with pytest.raises(ValueError):
        first_list.add_recipe(Recipe("Пицца",[Ingredient("Мука",100,"г"),Ingredient ("Курица",200,"г"), Ingredient("Томат", 300, "г")]),-666.0)
def test_remove_recipe():
    first_list = ShoppingList()
    first_list.add_recipe(Recipe("Пицца", [Ingredient("Мука", 100, "г"), Ingredient("Курица", 200, "г"), Ingredient("Томат", 300, "г")]),3.0)
    first_list.add_recipe(Recipe("Эчпочмак",[Ingredient("Тесто", 500, "г"), Ingredient("Мясо",600,"г")]),2.0)
    first_list.remove_recipe("Пицца")
    assert len(first_list._items) == 2
    assert first_list._items[0][1] == "Эчпочмак"
def test_remove_recipe_not_existed():
    first_list = ShoppingList()
    first_list.add_recipe(Recipe("Пицца", [Ingredient("Мука", 100, "г"), Ingredient("Курица", 200, "г"), Ingredient("Томат", 300, "г")]),3.0)
    first_list.add_recipe(Recipe("Эчпочмак",[Ingredient("Тесто", 500, "г"), Ingredient("Мясо",600,"г")]),2.0)
    first_list.remove_recipe("Кока-кола")
def test_get_list_sum_of_ingredients():
    first_list = ShoppingList()
    first_list.add_recipe(Recipe("Пицца", [Ingredient("Мука", 100, "г"), Ingredient("Курица", 200, "г"), Ingredient("Томат", 300, "г")]),3.0)
    first_list.add_recipe(Recipe("Эчпочмак", [Ingredient("Мука", 500, "г"), Ingredient("Мясо", 600, "г")]), 2.0)
    result = first_list.get_list()
    assert result[1].name=="Мука"
    assert result[1].quantity==1300
def test_get_list_sorted():
    first_list = ShoppingList()
    first_list.add_recipe(Recipe("Пицца", [Ingredient("Мука", 100, "г"), Ingredient("Курица", 200, "г"), Ingredient("Томат", 300, "г")]),3.0)
    first_list.add_recipe(Recipe("Эчпочмак", [Ingredient("Мука", 500, "г"), Ingredient("Мясо", 600, "г")]), 2.0)
    result = first_list.get_list()
    assert result[0].name == "Курица"
    assert result[1].name == "Мука"
    assert result[2].name == "Мясо"
    assert result[3].name == "Томат"
def test_add():
    first_list = ShoppingList()
    second_list = ShoppingList()
    first_list.add_recipe(Recipe("Пицца", [Ingredient("Мука", 100, "г"), Ingredient("Курица", 200, "г"), Ingredient("Томат", 300, "г")]),3.0)
    second_list.add_recipe(Recipe("Эчпочмак", [Ingredient("Мука", 500, "г"), Ingredient("Мясо", 600, "г")]), 2.0)
    full_list = first_list.__add__(second_list)
    assert len(full_list._items)==5
    assert full_list._items[-1][1] == "Эчпочмак"
    assert full_list._items[0][1] == "Пицца"
def test_add_lists_not_changed():
    first_list = ShoppingList()
    second_list = ShoppingList()
    first_list.add_recipe(Recipe("Пицца", [Ingredient("Мука", 100, "г"), Ingredient("Курица", 200, "г"), Ingredient("Томат", 300, "г")]),3.0)
    second_list.add_recipe(Recipe("Эчпочмак", [Ingredient("Мука", 500, "г"), Ingredient("Мясо", 600, "г")]), 2.0)
    full_list = first_list.__add__(second_list)
    assert len(first_list._items) == 3
    assert first_list._items[0][1] == "Пицца"
    assert len(second_list._items) == 2
    assert second_list._items[0][1] == "Эчпочмак"
























