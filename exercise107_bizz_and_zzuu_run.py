from exercise107_bizz_and_zzuu_functions import *

# Here we run the game (functions)

# Calling the functions
# print('Welcome to the BIZZUU Game')
# num = int(input('Please choose a number: '))

while num % 5 != 0 and num % 3 != 0:
    print(chosen_number(num))
    num = int(input('Please choose a number: '))
    num



final_output = run(num)
print(final_output)

