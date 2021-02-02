
def QuitOrConvert():
    r = str(input("C to convert, q to quit"))
    if r.lower() == ("c"): #x.lower() converts str to lowercase
        tempConverter()
    else: bye()

def tempConverter():
    f = float(input("degrees f"))
    c = (f - 32.0)*(5/9)
    print(c)
    QuitOrConvert()
    
    
def bye():
    print("Bye!")
    SystemExit
    

QuitOrConvert()
#tempConverter()


