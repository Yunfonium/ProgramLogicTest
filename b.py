def threeSumGroups(numList):
    result = set()
    n, p ,z = [],[],[]
    for i in numList:
        if i > 0:
            p.append(i)
        elif i < 0:
            n.append(i)
        else:
            z.append(i)
    N, P = set(n), set(p)
    
    if z:
        for num in P:
            if num*-1 in N:
                result.add((num*-1,0,num))
                
    if len(z) >= 3:
        result.add((0,0,0))
    
    for i in range(len(n)):
        for j in range(i+1, len(n)):
            target = -1*(n[i]+n[j])
            if target in P:
                result.add(tuple(sorted([n[i],n[j],target])))

    for i in range(len(p)):
        for j in range(i+1, len(p)):
            target = -1*(p[i]+p[j])
            if target in N:
                result.add(tuple(sorted([p[i],p[j],target])))
    result = list(list(item) for item in result)
    return result



if __name__ == '__main__':
    numList = input('Input a list of numbers, like [-1,0,3] : ')
    if '[' in numList:
        numList = numList.replace('[','')
    if ']' in numList:
        numList = numList.replace(']','')
    numList = numList.split(',')
    numList = [int(item) for item in numList]
    print('The three sum groups are: ', threeSumGroups(numList))