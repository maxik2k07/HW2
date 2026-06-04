from recipes import Ingredient
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


