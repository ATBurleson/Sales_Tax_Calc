# import datetime ------- This imports the date and time library so the program will display the date and
#                        time to the user.
import datetime
import locale

"""
Program: Calc.py 
Developer: Austin Burleson 
Purpose: Create a calculator program in python to gather the items the 
         user intends to purchase, next the gather the price of each item, take the prices entered be the user and sales tax, 
         but first the user must be prompted to enter the sales tax for the state he/she lives in and finale calculate the 
         total cost based from the sales tax calculated. 
Data: 12/30/2019 
"""
# ####################################################################################################################################################
# variable name = " "
name = " "
# NumberOfItems = 0 ----- create a number of items variable and set equal to zero
NumberOfItems = 0
# UsersAnswer = " " ----- create a variable to hold the answer the user give on whether they will make
#                         a purchase.
UsersAnswer = " "
# DateAndTime = datetime.datetime.now() ----- make a variable to hold the current date and time.
DateAndTime = datetime.datetime.now()
# ItemNames = [] --- array to hold user item names
ItemNames = []
# ItemPrice = [] --- array to hold user item prices
ItemPrice = []
# Tax = 0.0
Tax = 0.0
# subtotal = 0.0
subtotal = 0.0
# total = 0.0
total = 0.0
# y = "yes"
y = "yes"
# n = "no"
n = "no"

UsersAnswer = input("Do you plan on going to the store to make a purchase(s) -- type y for yes other no: ")
if UsersAnswer == "y":
    """
    here, the user will be presented the information, such as the program, Developer, 
    Purpose, and the date the program was created.
 
    The program will also include a function that will display the date and time as the user 
    opens the program by import datetime
    """
    print("Program: Calc.py ")
    print("Developer: Austin Burleson ")
    print("Purpose: Create a calculator program in python to gather the items the")
    print(
        "         user intends to purchase, next the gather the price of each item, take the prices entered be the user and sales tax,")
    print(
        "         but first the user must be prompted to enter the sales tax for the state he/she lives in and finale calculate the")
    print("        total cost based from the sales tax calculated. ")
    print("Data created: 12/30/2019 ")
    print(DateAndTime)
else:
    exit()

name = input("first, enter the name for who is making the the purchase:")
"""
next, ask the user if they plan on going to the store to purchase items, if so, ask for the 
quantity of items by the NumberOfItems = input("Please enter the item number").
"""
print("-------------------------------------------------------------------------------------------")
NumberOfItems = int(input("how many items do you plan to purchase: "))

"""
i = 0 --- create variable to count
while i <= NumberOfItems: --- use a while loop to loop through 
i += 1 ---increment i by 1

after asking the user if they plan on going to the store to purchase items, ask the user for the name
of each item by using ItemNames.append(input("Enter item# name:")).

x = 0
while x <= ItemName:
x += 1
ask the user for the name of each item entered.

after asking the user to enter the item names, have the user enter the prices
ItemPrice.append(input("Enter item " + ItemName[1] + " Price: "))
"""
i = 0
while i < NumberOfItems:
    i += 1
    ItemNames.append(input("Enter item " + str(i) + " name: "))

print(ItemNames)

"""
Create a for loop to calculate the total cost of the item
y =0
y += 1
while y <= ItemPrice:
    subtotal += ItemPrice[y]

print("total")
now that the total has been calculated, calculate the sales tax and that amount to total
ask the user their state sales tax:
state_sales_tax = input("enter your state sales tax amount: ")

print("") --- format

tax = subtotal * state_sales_tax
add tax to subtotal
total = subtotal +  tax
print("your total cost, with state sales tax, is" + total)

"""
x = 0
while x < NumberOfItems:
    x += 1
    ItemPrice.append(float(input("Enter item " + str(x) + " Price: ")))

print(ItemPrice)

Tax = input("Please enter the sales tax of the state you live in:")
print("The users sales tax for their state is " + Tax + "%")
print("The purchaser name is: " + name)
print("subtotal is: ", sum(ItemPrice))
print("tax is:", sum(ItemPrice) * float(Tax))
print("total is: ", (sum(ItemPrice) * float(Tax)) + sum(ItemPrice))
