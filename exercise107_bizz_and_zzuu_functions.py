# Functions go here

def chosen_number(num):
    if num % 5 == 0 and num % 3 == 0:
        return 'BIZZUUU'
    elif num % 3 == 0:
        return 'This is a Bizz Number'
    elif num % 5 == 0:
        return 'This is a Zzuu Number'
    else:
        return 'Try again'
print(chosen_number(num))
