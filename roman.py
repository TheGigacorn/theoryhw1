def roman_expander(base_roman):
    new_roman= []
    lim = len(base_roman)
    i = 0
    while i < lim:
        if (i == lim and base_roman[i] == 'I' and base_roman[i+1] == 'V'):
            new_roman.append('IIII')
            i=i+1
        elif (base_roman[i] == 'I' and base_roman[i+1] == 'X' and i != lim):
            new_roman.append('VIIII')
            i=i+1
        elif (base_roman[i] == 'X' and base_roman[i+1] == 'L' and i != lim):
            new_roman.append('XXXX')
            i=i+1
        elif (base_roman[i] == 'X' and base_roman[i+1] == 'C' and i != lim):
            new_roman.append('LXXXX')
            i=i+1
        elif (base_roman[i] == 'C' and base_roman[i+1] == 'D' and i != lim):
            new_roman.append('CCCC')
            i=i+1
        elif (base_roman[i] == 'C' and base_roman[i+1] == 'M' and i != lim):
            new_roman.append('MCCCC')
            i=i+1
        else:
            new_roman.append(base_roman[i])
        i+=1

    new_roman = ', '.join(new_roman)
    new_roman = new_roman.replace(', ', '')
    return new_roman

def roman_adder(roman_1, roman_2):
    comb_roman = roman_1 + roman_2
    


roman_num_1 = input("First number? \n")
roman_num_2 = input("Second number? \n")
print('\n')
print(roman_num_1)
print(roman_num_2)
roman_1 = roman_expander(roman_num_1)
roman_2 = roman_expander(roman_num_2)
print(roman_adder(roman_1, roman_2))

