item1 = float( input("Please enter the of the first item: "))
item2 = float( input("Please enter the of the second item: "))
item3 = float( input("Please enter the of the third item: "))
item4 = float( input("Please enter the of the fourth item: "))
item5 = float( input("Please enter the of the fifth item: "))

subTotal = item1 + item2 + item3 + item4 + item5

tax = 0.10 * subTotal

total = subTotal + tax

print("Sub total: $" + format( subTotal, ",.2f" ), "Tax amount: $" + \
      format( tax ,",.2f" ), "Total: $" + format( total, ",.2f" ), \
      sep ="\n" )

# 4. Total Purchase
# A customer in a store is purchasing five items. Write a program that asks for
# the price of each item, and then displays the subtotal of the sale, the
# amount of sales tax, and the total. Assume the sales tax is 10 percent.