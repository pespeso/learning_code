import re
import calendar
from datetime import datetime

# contemplo que los separadores de la fecha puedan ser "/" "-" o " "
# ejemplo de fecha correcta 25-08-2020 12:59:20

reg_ex = re.compile( r'^([0-2][0-9]|3[0-1])(\/|-|\s)(0[1-9]|1[0-2])(\/|-|\s)(\d{4})\s()([0-1][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$' )

def insert_date():
    '''Esta función solicita una fecha con un formato determinado y la valida por medio de expresiones regulares'''

    input_date = input ("Insert a date whit a format like this: 31/12/2020 23:59:59 \n" ).strip()
    result = reg_ex.match( input_date ) 

    while result == None: # Mientras el resultado de la validación sea None se continuará pidiendo la fecha
        print( "The input not have the format required\n" )
        input_date = input( "Insert a date whit a format like this: 31/12/2020 23:59:59\n" ).strip()
        result = reg_ex.match( input_date )
    else:
        return input_date

def transfor_input_in_date(input_date):
    ''' Función que transforma una fecha en formato string de dd/mm/yyyy HH:MM:SS a un objeto datetime '''

    input_date = input_date.replace( "-", "/" ).replace( " ", "/" ) # Unifico el formato de la fecha para dividirla
    
    day = int(input_date.split("/")[0])
    month = int(input_date.split("/")[1])
    year = int(input_date.split("/")[2])
    hour = int(input_date.split("/")[3].split(":")[0])
    minutes = int(input_date.split(":")[1])
    seconds = int(input_date.split(":")[2])
    
    input_date = datetime(year, month, day, hour, minutes, seconds) # Con los datos divididos, creo un objeto datetime

    return datetime(year, month, day, hour, minutes, seconds)

def print_date( input_date ):
    input_original = input_date
    input_date = transfor_input_in_date(input_date)
    day_of_week = calendar.day_name[datetime.weekday(input_date)]
    
    print( "\nYour input is", input_original )
    print( "That means we are in the year", input_date.year, "month", input_date.month, "and day", input_date.day )
    print( "and today is", day_of_week, "It's", str(input_date.hour)+":"+str(input_date.minute), "and", input_date.second, "seconds" )
    print( "We are ", datetime.timestamp(input_date), "seconds from 1970.\n" )
    
