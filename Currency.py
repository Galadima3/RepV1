RATE = 550


def ConverterDollar(value):
    newValue = value * RATE
    print(f'${value} is = ₦{newValue}')


def ConverterNaira(value):
    newValue = value / RATE
    print(f'₦{value} = ${newValue}')

Input = int(input('Enter 1 to Convert Dollars to Naira || Enter 2 to convert Naira to Dollars: \n'))
 
if (Input == 1):
     ValueDollar = float(input('Input value of dollars for conversion: '))
     ConverterDollar(ValueDollar)
    
elif(Input == 2):
    ValueNaira = float(input('Input value of Naira for conversion: '))
    ConverterNaira(ValueNaira)