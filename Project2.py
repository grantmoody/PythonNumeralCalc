#Garrett Moody, 11/6/2021, Code Reviewer

while(True):
    roman_chars = set(['I', 'V', 'X', 'L', 'C'])
    roman_map = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100}
    roman_num1 = input("Enter first roman numeral: ")
    roman_num2 = input("Enter second roman numeral: ")
    num1 = 0
    num2 = 0

    if not roman_num1.isupper() or not roman_num2.isupper():
        print("Need to enter in all caps!")
        continue
    
    isError = False
    #check to ensure just roman numerals
    for letter in roman_num1:
        if letter not in roman_chars:
            isError = True
            break
    for letter in roman_num2:
        if letter not in roman_chars:
            isError = True
            break
    
    if isError:
        print("Please enter valid roman numeral characters!\n")
        continue

    roman_num1 = roman_num1[::-1]
    roman_num2 = roman_num2[::-1]

    for i in range (len(roman_num1)):
        if i == 0 or roman_map[roman_num1[i]] >= roman_map[roman_num1[i-1]]:
            num1 += roman_map[roman_num1[i]]
        else:
            num1 -= roman_map[roman_num1[i]]

    for i in range (len(roman_num2)):
        if i == 0 or roman_map[roman_num2[i]] >= roman_map[roman_num2[i-1]]:
            num2 += roman_map[roman_num2[i]]
        else:
            num2 -= roman_map[roman_num2[i]]

    num3 = num1 + num2

    num_to_rom = {300:'CCC', 200:'CC', 100:'C', 
    90:'XC', 80:'LXXX', 70:'LXX', 60:'LX', 50:'L', 40:'XL', 30:'XXX', 20:'XX', 10:'X',
    9:'IX', 8:'VIII', 7:'VII', 6:'VI', 5:'V', 4:'IV', 3:'III', 2:'II', 1:'I'}


    new_rom = ''
    if num3 >= 100:
        new_rom += num_to_rom[(num3 // 100) * 100]
        num3 -= ((num3 // 100) * 100)
    if num3 >= 10:
        new_rom += num_to_rom[(num3 // 10) * 10]
        num3 -= ((num3 // 10) * 10)
    if num3 > 0:
        new_rom += num_to_rom[(num3)]
    print(new_rom)

    again = input("\nWould you like to do another computation? (Y/N): ")
    if again == 'y' or again == 'Y':
        continue
    else:
        break
