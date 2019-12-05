# Functions go here

print('Welcome to the BIZZUU Game')
num = int(input('Please choose a number: '))

def div_3(num):
    return num % 3 == 0

def div_5(num):
    return num % 5 == 0

def chosen_number(num):
    if div_5(num) and div_3(num):
        return 'BIZZUUU'
    elif div_3(num):
        return 'This is a Bizz Number'
    elif div_5(num):
        return 'This is a Zzuu Number'
    else:
        return 'Try again'

def run(num):
    output = chosen_number(num)
    return output
