Austin Vitagliano

The production function takes all items in a list of dataclasses and calculates the total amount that the user will be 
charged, including sales tax for the states MA, ME, and NH.

The function also takes into account special cases of the sales tax laws across those three states, such as clothing in MA and groceries in ME.

The calculations are done as follows: 

The function iterates through a list of items the user is purchasing, and checks if sales tax is applicable to each item. 
If it is, the sales tax is calculated for the item and added to its price, which is then added to the total price of all the items.
If sales tax is exempt from the item in question, then the item's price is just added to the total price with no sales tax 
calculations.

If there is an item with a negative price in the list and/or an item with an invalid type that isn't 
"Wic Eligible Food", "Clothing", or "Everything Else", the program notifies the user in console, and the program aborts 
stating the problem with code -1 or -2 depending on the problem.

The tests are run by running the Python file 'test_price_calculations_with_sales_tax.py' with pytest.
The venv folder is not included here for obvious reasons.


