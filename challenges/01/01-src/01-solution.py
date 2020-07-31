from datetime import datetime

txt1 = "Today is:"
txt2 = "Have a nice day."
strFormat = "%H:%M:%S - %d/%m/%y"

formatedDate = datetime.strftime(datetime.now(), strFormat)

print(txt2 + " " + txt1 + " " + formatedDate)
print(txt2, txt1, formatedDate)

