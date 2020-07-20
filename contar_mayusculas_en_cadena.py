# Escribir un programa que cuente las mayusculas de una cadena de caracteres

frase=(input("Introduzca una cadena de texto: "))
cont=0
for i in frase:
    if i !=i.lower():
        cont+=1  
 
print("Hay ",cont," mayusculas en la cadena de texto")  