import random as rnd
from math import sqrt

def getFiveNumbersList() -> str:
    number_list = []
    while len(number_list) < 5:
        number = rnd.randint(0,9)
        if number not in number_list :
            number_list.append(number)
        else:
            continue
    number_list = sorted(number_list)
    print('The random 5 numbers are :', number_list)
    return number_list

def permute(number_list):
    fiveDigitsList = []
    l = len(number_list)
    def backtrack(id):
        if (id == l):
            if (number_list[0]!=0):
                fiveDigitsList.append(number_list[:])
            return 
        for i in range(id,l):
            number_list[id],number_list[i] = number_list[i], number_list[id]
            backtrack(id + 1)
            number_list[id],number_list[i] = number_list[i], number_list[id]
    
    backtrack(0)        
    return fiveDigitsList

def numListToInt(numList):
    number = 0
    for curr_digits in numList:
        number = number*10 + curr_digits
    return number

def findMaxMinAndPrime(number_list):
    maximum = max(number_list)
    minimum = min(number_list)
    prime_list= []
    for num in number_list:
        if checkFiveDigitsPrime(num):
            prime_list.append(num)
    
    return maximum, minimum, prime_list

def checkFiveDigitsPrime(num) -> bool:
    if num%2 == 0:
        return False
    for i in range(3,int(sqrt(num)+1)):
        if num % i == 0:
            return False
    return True
        

if __name__ == '__main__':
   n_list = getFiveNumbersList()
   print('選到的五個數字是: ',n_list)
   numberList = []
   permuted_n_list = permute(n_list)
   for n in permuted_n_list:
        n = numListToInt(n)
        numberList.append(n)
   print('所有可能排列出的五位數是: ',numberList)
   maximum, minimum, prime_lis = findMaxMinAndPrime(numberList)
   print('最大是: ',maximum)
   print('最小是: ',minimum)
   print('質數是: ',prime_lis)
   
   