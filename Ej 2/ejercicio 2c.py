
# muestra la suma de los N mueros pares


suma=0
numeroFinal=0 #(se pide por teclado) 

numeroFinal=int(input("valores que quieres sumar"))

for numero in range(0,numeroFinal*2 ,2):#se multiplica por 2 para sumar los 50 primeros numero, que serian del  0 al 100
   print("numero par : ",end="" )
   print(numero)
   suma = suma + numero 

print(suma)   