import funcionesmath as fmath
from datetime import date
  
while True:
    today = date.today()
    print(today)
    print("<<<Autor: Jose Maximiliano Mora Sepulveda>>>")
    print("seleciona algun numero:")
    print("1 Suma")
    print("2 Resta")  
    print("3 Multiplicacion")
    print("4 Divicion")
    print("5 Menu") 
    print("6 salir")
    selecion = int(input())  

    def numeros(): 
          print("digita los numeros")
          num1 = int(input())
          num2 = int(input())
          return num1, num2
    
    if selecion == 1:
        num1, num2 = numeros()
        print("La Suma de tus numeros es:", fmath.suma(num1, num2))
              
    elif selecion == 2:
        num1, num2 = numeros()
        print("La Resta de tus numerons es :", fmath.resta(num1, num2))
    elif selecion == 3:
        num1, num2 = numeros()
        print("La Multiplicasion es:", fmath.multiplicasion(num1, num2))
    elif selecion == 4:
        num1, num2 = numeros()
        print("La Divicion es:", fmath.division(num1, num2))
    elif selecion == 5:
        continue
    elif selecion == 6:
        print("Gracias por entrar a la Calculadora")
        break