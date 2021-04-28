from dataclasses import dataclass


@dataclass
class shopping_item:
    name: str
    price: float
    type: str


list_items = [shopping_item("banana", 1.00, "Wic Eligible Food"), shopping_item("shirt", 20.00, "Clothing"),
              shopping_item("suit", 200.00, "Clothing"), shopping_item("paper", 5.00, "Everything Else")]


def total_price_with_sales_tax(states, list_items):
    sales_tax_MA = .0625
    ME_sales_tax = 0.055
    total_price = 0.0
    if states == "MA":
        for shopping_items in list_items:
            # Don't allow negative prices, exit program and print to console if one is found
            if shopping_items.price < 0.0:
                print("No negative values allowed; can't process refunds.")
                raise SystemExit(-1)
            # apply sales tax normally to wic eligible food and everything else
            elif shopping_items.type == "Wic Eligible Food" or shopping_items.type == "Everything Else":
                item_tax = shopping_items.price * sales_tax_MA
                item_total_price = item_tax + shopping_items.price
                total_price = total_price + item_total_price
            # in MA, there's a policy that casual clothing below $175 does not apply for sales tax.
            elif shopping_items.type == "Clothing" and shopping_items.price <= 174.99:
                item_total_price = shopping_items.price
                total_price = total_price + item_total_price
            # in MA, there's a policy that a single piece of clothing over $175 is applicable for sales tax
            # on the amount that goes over $175 see here:
            # https://www.mass.gov/guides/sales-and-use-tax#:~:text=Clothing%20is%20generally%20exempt%20from,of%20the%20taxable%20%2425%20difference).
            elif shopping_items.type == "Clothing" and shopping_items.price >= 175.00:
                item_tax = (shopping_items.price - 175.00) * sales_tax_MA
                item_total_price = item_tax + shopping_items.price
                total_price = total_price + item_total_price
            # check for invalid item type in list, raise exception if it finds one
            else:
                print("Item has invalid type.")
                raise SystemExit(-2)
        return round(total_price, 2)
    elif states == "ME":
        for shopping_items in list_items:
            # Don't allow negative prices, raise exception if it does
            if shopping_items.price < 0.0:
                print("No negative values allowed; can't process refunds.")
                raise SystemExit(-1)
            # Maine does not apply sales tax to Wic Eligible food when it's groceries,
            # see here here: https://www.salestaxhandbook.com/maine
            elif shopping_items.type == "Wic Eligible Food":
                item_total_price = shopping_items.price
                total_price = total_price + item_total_price
            # Apply sales tax normally for clothing and everything else
            elif shopping_items.type == "Clothing" or shopping_items.type == "Everything Else":
                item_tax = shopping_items.price * ME_sales_tax
                item_total_price = shopping_items.price + item_tax
                total_price = total_price + item_total_price
            # check for invalid item type in list, raise exception if it finds one
            else:
                print("Item has invalid type.")
                raise SystemExit(-2)
        return round(total_price, 2)
    else:
        for shopping_items in list_items:
            # Don't allow negative prices, raise exception if it does
            if shopping_items.price < 0.0:
                print("No negative values allowed; can't process refunds.")
                raise SystemExit(-1)
            # NH does not have sales tax, so just add prices up
            elif shopping_items.type == "Clothing" or shopping_items.type == "Wic Eligible Food" \
                    or shopping_items.type == "Everything Else" and shopping_items.price >= 0.0:
                total_price = total_price + shopping_items.price
            # check for invalid item type in list, raise exception if it finds one
            else:
                print("Item has invalid type.")
                raise SystemExit(-2)
        return round(total_price, 2)


if __name__ == '__main__':
    print(total_price_with_sales_tax(states="MA", list_items=list_items))
    print(total_price_with_sales_tax(states="ME", list_items=list_items))
    print(total_price_with_sales_tax(states="NH", list_items=list_items))
