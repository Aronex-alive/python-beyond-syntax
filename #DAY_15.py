import time  
a=time.strftime('%H%M%S')     # the usage of time module to get current time in HHMMSS format
a=int(a)
if a<120000:
    print("Good Morning")
elif a>120000 and a<170000:   
    print("Good Afternoon")
elif a>170000 and a<210000:
    print("Good Evening")
elif a==120000 or a==000000:
    print("It's Noon")    
else:
    print("Good Night")            