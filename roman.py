def roman_expander(base_roman):
    new_roman= []
    lim = len(base_roman)
    i = 0
    print(lim)
    while i < lim:
        print(i)
        if i + 1 == lim:
            new_roman.append(base_roman[i])
            break
        elif (i < lim and base_roman[i] == 'I' and base_roman[i+1] == 'V'):
            new_roman.append('IIII')
            i=i+1
        elif (i <= lim and base_roman[i] == 'I' and base_roman[i+1] == 'X'):
            new_roman.append('VIIII')
            i=i+1
        elif (i <= lim and base_roman[i] == 'X' and base_roman[i+1] == 'L'):
            new_roman.append('XXXX')
            i=i+1
        elif (i <= lim and base_roman[i] == 'X' and base_roman[i+1] == 'C'):
            new_roman.append('LXXXX')
            i=i+1
        elif (i <= lim and base_roman[i] == 'C' and base_roman[i+1] == 'D'):
            new_roman.append('CCCC')
            i=i+1
        elif (i <= lim and base_roman[i] == 'C' and base_roman[i+1] == 'M'):
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
        
    return total_list

def roman_subtract(roman_num1, roman_num2):
    count_1 = roman_counter(roman_num1)
    long_roman1 = roman_deconstruct(roman_num1, count_1)
    count_2 = roman_counter(roman_num2)
    long_roman2 = roman_deconstruct(roman_num2, count_2)

    long_count1 = roman_counter(long_roman1)
    long_count2 = roman_counter(long_roman2)

    if (min(long_count1[0], long_count2[0]) != 0):
        long_roman1 = long_roman1.replace('M', '', min(long_count1[0], long_count2[0]))
    if (min(long_count1[1], long_count2[1]) != 0):
        long_roman1 = long_roman1.replace('D', '', min(long_count1[1], long_count2[1]))
    if (min(long_count1[2], long_count2[2]) != 0):
        long_roman1 = long_roman1.replace('C', '', min(long_count1[2], long_count2[2]))
    if (min(long_count1[3], long_count2[3]) != 0):
        long_roman1 = long_roman1.replace('L', '', min(long_count1[3], long_count2[3]))
    if (min(long_count1[4], long_count2[4]) != 0):
        long_roman1 = long_roman1.replace('X', '', min(long_count1[4], long_count2[4]))
    if (min(long_count1[5], long_count2[5]) != 0):
        long_roman1 = long_roman1.replace('V', '', min(long_count1[5], long_count2[5]))
    if (min(long_count1[6], long_count2[6]) != 0):
        long_roman1 = long_roman1.replace('I', '', min(long_count1[6], long_count2[6]))

    return long_roman1



def roman_deconstruct(roman_num, count):
    i=0
    for i in range(len(count)):
        print(i)
        if count[i] > 0:
            if i == 0:
                roman_num = roman_num.replace('M', 'DD')
            elif i == 1:
                roman_num = roman_num.replace('D', 'CCCCC')
            elif i == 2:
                roman_num = roman_num.replace('C', 'LL')
            elif i == 3:
                roman_num = roman_num.replace('L', 'XXXXX')
            elif i == 4:
                print('here')
                roman_num = roman_num.replace('X', 'VV')
            elif i == 5:
                roman_num = roman_num.replace('V', 'IIIII')

    return roman_num




roman_num_1 = input("First number? \n")
roman_num_2 = input("Second number? \n")
print('\n')
print(roman_num_1)
print(roman_num_2)
roman_1 = roman_expander(roman_num_1)
roman_2 = roman_expander(roman_num_2)
print('heehee')
print(roman_1)
print(roman_2)
#print(roman_adder(roman_1, roman_2))
print(roman_subtract(roman_1, roman_2))

