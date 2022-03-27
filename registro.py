from datetime import datetime , date , time
from time import strptime
from traceback import format_tb


in_deseado = "14:00"
out_deseado = "21:00"

def conversor(a):
    hora_formateada = datetime.strptime(a, '%H:%M')
    print(hora_formateada)

conversor("13:30")