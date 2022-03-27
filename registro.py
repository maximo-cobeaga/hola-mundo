from datetime import datetime , date , time
from time import strptime
from traceback import format_tb


formato_hora = "%H:%M"

# Conversion a tipo datetime 
in_ = datetime.strptime("14:00", formato_hora)
out_ = datetime.strptime("21:00", formato_hora)

#Recortes de las variables
in_formated = in_.strftime(formato_hora)
out_formated = out_.strftime(formato_hora)

#Entrada de datos
user_in = input('\n¿A que hora ingresaste?   -->  ')
user_out = input('\n¿A que hora saliste?     -->  ')

#Conversor a tipo datetime de la entrada de datos
user_in_f = datetime.strptime(user_in,formato_hora)
user_out_f = datetime.strptime(user_out,formato_hora)

#Recorte de las variables 
user_in_formated = user_in_f.strftime(formato_hora)
user_out_formated = user_out_f.strftime(formato_hora)

#Condicional para comprobar horarios de entrada
if user_in_formated != in_formated:
    print('\nEstas en al hora equivocada\n')
else: 
    print('\nEstas en la hora correcta\n')

#Condicional para comprobar horarios de salida
if user_out_formated != out_formated:
    print('Estas en al hora equivocada\n')
else: 
    print('Estas en la hora correcta\n')




