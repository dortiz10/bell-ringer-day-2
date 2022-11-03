
coffee_prices =[('cappucino', 1.5,),
               ('expresso',1.2),
               ('mocha',1.9)]

#problem #1 retrieve the coffee names and price from the above tuple. Make sure it is in a readable format(hint: f strings)
# from coffe_prices import coffePrices
# from highestcoffee import expensive

# coffePrices()
# expensive()

# coffeePrices = coffee_prices
# print(f"the coffe we have in stock are{coffee_prices}"[0:-1])


#create a function that iterates through the tuple list above and returns the highest priced coffee only. You probably want to create a function that has arguments  

# (average, smallest, highest) = coffee_prices

# print(f'Our high valued coffee available is {highest}')


for coffee, price in coffee_prices:
  print(f" Coffe name: {coffee} and price is {price}")

def most_expensive_coffee(coffee_prices):
  #establish what the highest prices are my most expensive coffee
  highest_price = 0
  my_most_expensive_coffee = ""

  for coffee, price in coffee_prices:
    if price > highest_price:
      highest_price = price
      my_most_expensive_coffee = coffee
    else:
      pass
  return(my_most_expensive_coffee, highest_price)

print(most_expensive_coffee(coffee_prices))
