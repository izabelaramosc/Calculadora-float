while True:

 numero_1 = input ('digite um numero: ')
 numero_2 = input ('digite outro numero: ')
 operador = input ('digite o operador +-*/: ')


 numeros_validos= None
 num_1_float = 0
 num_2_float = 0


 try:
   num_1_float = float (numero_1)
   num_2_float = float (numero_2)
   numeros_validos = True

 except:
   numeros_validos = None

   if numeros_validos is None:
     print ('Não é um numero validos')
     continue

 operadores_permitidos = '+-*/'

 if operador not in operadores_permitidos:
     print ('não esta entre os operadores permitidos')
     continue

 if len(operador) > 1:
     print ('digite apenas um operador')
     continue 
 
 ###

 if operador == '+':
   print (f'{num_1_float} + {num_2_float} = ' , num_1_float + num_2_float)

 elif operador == '-':
   print (f'{num_1_float} - {num_2_float} = ' , num_1_float - num_2_float)

 elif operador == '/':
   print (f'{num_1_float} / {num_2_float} = ' , num_1_float / num_2_float)

 elif operador == '*':
   print (f'{num_1_float} * {num_2_float} = ' , num_1_float * num_2_float)

 else:
    print ('não deveria chegar aqui')




 sair = input ('voce quer sair [s]im: ').lower().startswith ('s') 

 if sair is True:
   break 