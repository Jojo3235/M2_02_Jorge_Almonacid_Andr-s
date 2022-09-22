#Ejercicio 3
username = str(input("Esribe tu nombre de usuario: "))        #Creamos una entrada para definir las variables
password = str(input("Escribe tu Contraseña: "))
print(3<len(username)<10)                                     #Imprimimos si el username es mayor que 3 o menor que 10
print(password == "Tokio" or password == "Python")            #Imprimimos si password es Tokio o Python, devuelve True o False
