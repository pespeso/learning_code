from datetime import datetime

txt1 = "Today is:"
txt2 = "Have a nice day."

formatedDate = datetime.strftime(datetime.now(), '%H:%M:%S - %d/%m/%y')

print(txt2+" "+txt1+" "+formatedDate)
print(txt2,txt1,formatedDate)

