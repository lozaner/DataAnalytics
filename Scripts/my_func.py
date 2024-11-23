
product_price = 12.0
product_qty = 5

#Ejemplo 1
def total_price_local_scope():
    product_price = 11.0  # Variable local
    product_qty = 4       # Variable local
    print(f'Precio total (local): {product_price * product_qty}')

# Ejemplo 2
def total_price_global_scope():
    print(f'Precio total (global): {product_price * product_qty}')

#Ejemplo 3
def trip_price(dist_miles, mpg, price, loc_from, loc_to):
    total_price = dist_miles * price / mpg
    print(f'Un viaje de {loc_from} a {loc_to} costará ${total_price}')

#Ejemplo 4
def trip_price(dist_miles, mpg, price, loc_from='A', loc_to='B'):
    total_price = dist_miles * price / mpg
    print(f'Un viaje de {loc_from} a {loc_to} costará ${total_price}')

#Ejemplo 5
def trip_price(loc_to='B', dist_miles, mpg, price, loc_from='A'):
    total_price = dist_miles * price / mpg
    print(f'Un viaje de {loc_from} a {loc_to} costará ${total_price}')
    #este ejemplo marcara error 





# Llamar ambas funciones
total_price_local_scope()
total_price_global_scope()
trip_price(409, 35, loc_from='Boston', loc_to='New York', price=5.1)
trip_price(409, 35, price=3.8)
trip_price(409, 35, price=3.8) # este marcara error 

#recordar para imprimir es: python + nombre del archivo que correremos
#python my_func.py