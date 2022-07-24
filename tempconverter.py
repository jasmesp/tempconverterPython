
def QuitOrConvert():
    r = str(input("C to convert, q to quit\n"))
    if r.lower() == ("c"): #x.lower() converts str to lowercase
        Celsius_or_Fah()
    else: bye()

def Celsius_or_Fah():
    c_or_f = str(input("C for celsius to fahrenheit, F for fahrenheit to Celsius\n"))
    if c_or_f.lower() == ("c"): #x.lower() converts str to lowercase
        c_to_f_converter()
    else: f_to_c_converter()

def f_to_c_converter():
    f = float(input("degrees f\n"))
    c = (f - 32.0)*(5/9)
    print(c)
    QuitOrConvert()


def c_to_f_converter():
    c = float(input("degrees c\n"))
    f = ((c * (9/5)) + 32.0)
    print(f)
    QuitOrConvert()


def bye():
    print("Bye!")
    SystemExit


QuitOrConvert()
#tempConverter()
