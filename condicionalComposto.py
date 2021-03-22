#Sintaxe da estrutura condicional composta

'''if ( 'Variavel Booleana' ):
    'codigo 1'
else:
    'codigo 2'''
    
#1

letraA = 0

if ( False ):
    letraA = 10
else:
    letraA = 20

print(letraA)

#2

variavelA = 30

if ( variavelA > 20 ):
    print("A variavel 'a' eh maior que 20")
else:
    print("A variavel 'a' NAO eh maior que 20")
    
    
#Sintaxe da estrutura condicional composta

'''if ( 'Variavel Booleana' ):
    'codigo 1'
elif ( 'Variavel Booleana' ):
    'codigo 2'
else:
    'codigo 3'''
    
#1

a = 0

if ( False ):
    a = 10
    print("Valor 10")
elif ( False ):
    a = 20
    print("Valor 20")
else:
    a = 30
    print("Valor 30")

print(a)