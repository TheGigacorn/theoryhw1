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
    
    valueOrder = "MDCLXVI"

    new_list = sorted(comb_roman, key=lambda word: [valueOrder.index(c) for c in word[0]])
    sorted_roman = ''.join(new_list)
    
    print(sorted_roman)
    
    count_list = roman_counter(sorted_roman)
    print(count_list)

    if (count_list[6]%5 == 0):
        sorted_roman = sorted_roman.replace('IIIII', 'V')

    if (count_list[5]%2 == 0):
        sorted_roman = sorted_roman.replace('VV', 'X')

    if (count_list[4]%5 == 0):
        sorted_roman = sorted_roman.replace('XXXXX', 'L')

    if (count_list[3]%2 == 0):
        sorted_roman = sorted_roman.replace('LL', 'C')

    if (count_list[2]%5 == 0):
        sorted_roman = sorted_roman.replace('CCCCC', 'D')

    if (count_list[1]%2 == 0):
        sorted_roman = sorted_roman.replace('DD', 'M')

    while (sorted_roman.find('MCCCC') != -1):
        sorted_roman = sorted_roman.replace('MCCCC', 'CM', 1)
        print(sorted_roman)

    while (sorted_roman.find('CCCC') != -1):
        sorted_roman = sorted_roman.replace('CCCC', 'CD', 1) 
        print(sorted_roman)

    while (sorted_roman.find('LXXXX') != -1):
        sorted_roman = sorted_roman.replace('LXXXX', 'XC', 1)
        print(sorted_roman)
        
    while (sorted_roman.find('XXXX') != -1):
        sorted_roman = sorted_roman.replace('XXXX', 'XL', 1)
        print(sorted_roman)

    while (sorted_roman.find('VIIII') != -1):
        sorted_roman = sorted_roman.replace('VIIII', 'IX', 1)

    while (sorted_roman.find('IIII') != -1):
        sorted_roman = sorted_roman.replace('IIII', 'IV', 1)

    return sorted_roman

def roman_counter(roman_num):
    total_list = [0,0,0,0,0,0,0]
    for i in roman_num:
        if i == 'M':
            total_list[0]+=1
        if i == 'D':
            total_list[1]+=1
        if i == 'C':
            total_list[2]+=1
        if i == 'L':
            total_list[3]+=1
        if i == 'X':
            total_list[4]+=1
        if i == 'V':
            total_list[5]+=1
        if i == 'I':
            total_list[6]+=1
        
    print(total_list)
    return total_list



roman_num_1 = input("First number? \n")
roman_num_2 = input("Second number? \n")
print('\n')
print(roman_num_1)
print(roman_num_2)
roman_1 = roman_expander(roman_num_1)
roman_2 = roman_expander(roman_num_2)
print(roman_adder(roman_1, roman_2))

