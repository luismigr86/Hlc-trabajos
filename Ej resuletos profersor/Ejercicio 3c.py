""" 	Introduciremos por teclado una matriz de 2 x 2, y nos devolverá el valor de su determinante  """

# declaracion de variables
fila=0 #recorre el  numero de filas 
col=0 #recorrela el numero  columnas
matriz = [[0,0],[0,0]]

determinante=0


#programa principal
for fila in range(0,2): # recorre las filas 
    for col in range(0,2): # recorre las colunmas
        matriz[fila][col]= int(input(f"introduce el elemento({fila},{col})de la matriz: "))

determinante = matriz[0][0] * matriz[1][1] - matriz[1][0] * matriz[0][1] 

print(f"El determinnate de la matriz es {determinante}")
