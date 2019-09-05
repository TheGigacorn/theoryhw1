def abacus_add(list1, list2):
    len1 = len(list1)
    len2 = len(list2)
    
    big_num = "1" + "0"*len2
    big_num = int(big_num, 10)
    compl = big_num - get_compliment(list2)
    
    numb1 = get_compliment(list1)

    answer = numb1 - compl
    answer = answer + big_num

    print("{}  -  {}  +  {}  =  {}".format(numb1, compl, big_num, answer))

    return answer
    
def get_compliment(a_list):
    temp = ', '.join(str(i) for i in list2)
    temp = temp.replace(', ', '')
    temp = int(temp,10)
    return temp




num1 = input("first num?\n")
num2 = input("secon num?\n")

list1 = [int(d) for d in str(num1)]
list2 = [int(d) for d in str(num2)]

print(abacus_add(list1, list2))


