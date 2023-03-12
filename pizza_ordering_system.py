import datetime                    
import os          






class MenuItem:
    
    
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        return self.name + ': $' + str(self.price)

    def get_total_price(self, count):
        total_price = self.price * count

      



class Pizza(MenuItem):
    def __init__(self, name, price, ):
    
        super().__init__(name,price)

    
    def info(self):
        return self.name + ': $' + str(self.price) 
   

class Materials(MenuItem):
   
    def __init__(self, name, price):
        super().__init__(name, price)
       
    
    def info(self):
        return self.name + ': $' + str(self.price)


pizza1 = Pizza('Classic Pizza', 8)
pizza2 = Pizza('Margaritta', 10)
pizza3 = Pizza('Turkish Pizza', 15)
pizza4 = Pizza('Simple Pizza', 12)

pizzas = [pizza1,pizza2,pizza3,pizza4]

metarial1 = Materials('Olive', 1)
metarial2 = Materials('Mushroom', 1)
metarial3 = Materials('Goat Cheese', 2)
metarial4 = Materials('Meat', 3)
metarial5 = Materials('Onion', 1)
metarial6 = Materials('Corn', 1)

metarials = [metarial1,metarial2,metarial3,metarial4,metarial5,metarial6]

print('Pizza')
index = 1
for pizza in pizzas:
    print(str(index) + '. ' + pizza.info())
    index += 1

print('Metarials')
index = 1
for metarial in metarials:
    print(str(index) + '. ' + metarial.info())
    index += 1

print('--------------------')

pizza_order = int(input('Enter pizza item number: '))
selected_pizza = pizzas[pizza_order]

metarial_order = int(input('Enter metarial item number: '))
selected_metarial = metarials[metarial_order]






print("Please, fill in the information below.")
name=input("Name:")
surname=input("Surname:")
ID=input("ID:")
adress=input("Adress:")
credit_card=input("Credit card number:")
print("Thanks for shopping!")

count=int(input('How many meals would you like to purchase? '))


result= str(selected_pizza.get_total_price(count)) + str(selected_metarial.get_total_price(count))



print('Your total is $'+str(result))





