dic = {} 
def pascal(x):
    if x == 1:
        dic[x] = {0: 1, 1: 1}
        return "1"
    else:
        dic[x] = {}
        dic[x][0] = 1
        for num in range(1,len(dic[x-1])): 
            dic[x][num] = dic[x-1][num] + dic[x-1][num-1]
        dic[x][x] = 1
        test = ' '.join(str(a) for a in dic[x].values())
        return test
        
for x in range(1, 101):
    row = pascal(x)
    print(row)
