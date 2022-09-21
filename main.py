#Ejericio 1
nota_1=8; nota_2=5; nota_3=7; nota_4=8; nota_5=9              #Definimos las notas en 5 variables distintas
nota_media=(nota_1+nota_2+nota_3+nota_4+nota_5)/5             #Definimos la nota media como la suma de las 5 /5
print(f"La nota media es {nota_media}")                       #Imprimimos una string que nos dice cual es la nota media

#Ejercicio 2
operacion = (365/12)*14.7                                     #Definimos la operación
print(round(operacion,2))                                     #Imprimimos la operación redondeada a dos decimales

#Ejercicio 3
username = str(input("Esribe tu nombre de usuario: "))        #Creamos una entrada para definir las variables
password = str(input("Escribe tu Contraseña: "))
print(3<len(username)<10)                                     #Imprimimos si username es mayor que 3 o menor que 10, devuelve True o False
print(password == "Tokio" or password == "Python")            #Imprimimos si password es Tokio o Python, devuelve True o False

#Ejercicio 4
num1=3;num2=15                                                      #Definimos los dos números como variables
num1+=1                                                             #Redefinimos el primer número como ese más 1
num2-=2                                                             #Redefinimos el segundo número como ese menos 2
num1*=3                                                             #Redefinimos el primer número de nuevo como ese por 3
num2*=2                                                             #Redefinimos el segundo número de nuevo como ese por 2
print(f"El primer número es: {num1} y el segundo: {num2}")          #Imprimimos ambos números y vemos como se han redefinido los valores