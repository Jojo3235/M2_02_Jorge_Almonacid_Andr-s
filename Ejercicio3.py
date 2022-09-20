#Ejercicio 3
username = str(input("Esribe tu nombre de usuario: "))        #Creamos una entrada para definir las variables
password = str(input("Escribe tu Contraseña: "))
if len(username) >= 3:                                        #Creamos una condición para que nos devuelva que la contraseña es True o False
  print("Usuario: True")                                      #Si la longitud de la palabra dentro de usuario es mayor a 3, entonces devuelve True
else:                                               
  print("Usuario: False")                                     #Si no nos devuelve False
if password == "Tokio" or "Python":                           #Lo mismo para la contraseña, pero en vez de la longitud, tiene que ser igual a Tokio o Python
  print("password: True")
else:
  print("password: False")