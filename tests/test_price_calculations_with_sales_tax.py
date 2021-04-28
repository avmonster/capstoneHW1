import sales_tax_calc
import pytest
from sales_tax_calc import shopping_item


# good data tests
# assert correct total value of items with sales tax was calculated for MA
def test_sales_tax_calculation_for_MA():
    list_items = [shopping_item("Banana", 1.00, "Wic Eligible Food"), shopping_item("shirt", 20.00, 'Clothing'),
                  shopping_item("suit", 200.00, 'Clothing'), shopping_item("paper", 5.00, 'Everything Else')]
    assert sales_tax_calc.total_price_with_sales_tax(states="MA", list_items=list_items) == 227.94


# assert correct total value of items with sales tax was calculated for ME
def test_sales_tax_calculation_for_ME():
    list_items = [shopping_item("Banana", 1.00, "Wic Eligible Food"), shopping_item("shirt", 20.00, 'Clothing'),
                  shopping_item("suit", 200.00, 'Clothing'), shopping_item("paper", 5.00, 'Everything Else')]
    assert sales_tax_calc.total_price_with_sales_tax(states="ME", list_items=list_items) == 238.38


# assert correct total value of items with sales tax was calculated for NH
def test_sales_tax_calculation_for_NH():
    list_items = [shopping_item("Banana", 1.00, "Wic Eligible Food"), shopping_item("shirt", 20.00, 'Clothing'),
                  shopping_item("suit", 200.00, 'Clothing'), shopping_item("paper", 5.00, 'Everything Else')]
    assert sales_tax_calc.total_price_with_sales_tax(states="NH", list_items=list_items) == 226.0


# bad data tests
# assert that the program aborted upon seeing negative price for one of the items in the list
def test_negative_numbers():
    list_items = [shopping_item("Banana", 1.00, "Wic Eligible Food"), shopping_item("shirt", 20.00, 'Clothing'),
                  shopping_item("suit", -200.00, 'Clothing'), shopping_item("paper", 5.00, 'Everything Else')]
    with pytest.raises(SystemExit) as e:
        sales_tax_calc.total_price_with_sales_tax(states="MA", list_items=list_items)
    assert e.type == SystemExit
    assert e.value.code == -1


# assert that program aborted upon seeing invalid item type for one of the items in the list
def test_invalid_item_type():
    list_items = [shopping_item("Banana", 1.00, "Fruit"), shopping_item("shirt", 20.00, 'Clothing'),
                  shopping_item("suit", 200.00, 'Clothing'), shopping_item("paper", 5.00, 'Everything Else')]
    with pytest.raises(SystemExit) as e:
        sales_tax_calc.total_price_with_sales_tax(states="MA", list_items=list_items)
    assert e.type == SystemExit
    assert e.value.code == -2
