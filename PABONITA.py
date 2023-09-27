# Input purchase amount for tax
Purchase_Tax = float(input("Purchase Tax:"))

# Input sales tax amount
sale = Purchase_Tax * 0.06
discount = "{:.2f}".format(sale)
print(discount)