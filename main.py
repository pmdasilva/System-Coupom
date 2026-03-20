lovely_loveseat_price = [{'nome':'lovely_loveseat','preco':254.00,'descricao':'Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.'}]
stylish_settee_price = [{'nome':'stylish_settee','preco':180.50,'descricao':'Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.'}]
luxurious_lamp_price = [{'nome':'luxurious_lamp','preco':52.15,'descricao':'Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.'}]
customer_one_total = 0

def cupom():
  print('Customer One Items:')
  print('#'*30)

def checkout():
  global customer_one_total
  customer_one_total += lovely_loveseat_price[0]['preco']
  customer_one_total += luxurious_lamp_price[0]['preco']
  print(f'Customer One Total: R${customer_one_total}')

# Adicionando o nome do item docomprado ao carrinho:
def add_to_cart(): 
  customer_one_itemization = []
  customer_one_itemization.append(lovely_loveseat_price[0]['nome'])
  customer_one_itemization.append(luxurious_lamp_price[0]['nome'])
  print(f'Customer One Items: {customer_one_itemization}')

# Calculando o imposto sobre produto
def sales_tax():
  global customer_one_total
  sales_tax = 0.088
  custom_one_tax = customer_one_total * sales_tax 
  print(f'Imposto sobre produto: {round(custom_one_tax,2)}')


cupom()
checkout()
add_to_cart()
sales_tax()