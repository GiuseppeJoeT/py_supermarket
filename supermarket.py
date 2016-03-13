prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

print ("The Supermarket prices and stock are: " + "\n")

for key in prices:
    print key
    print "price: %s " % prices[key]
    print "stock: %s " % stock[key]
    print " "

print (' ')

total = 0

print ("The Supermarket stock values is: " + "\n")

for key in prices:
    total += prices[key] * stock[key]
    print key + " : " + str(total) + " Euro"

print (' ')

# Shopping at the Market

shopping_list = ["banana", "orange", "apple"]


def compute_bill(food):
    total_bill = 0
    for item in food:
        if stock[item] > 0:
            total_bill += prices[item]
            stock[item] = stock[item] - 1
    return total_bill
