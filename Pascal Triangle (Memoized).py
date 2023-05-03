import timeit

dic = {} 
def pascal(x):
    if x == 0:
        dic[x] = {0:1}
        return "1"
    elif x == 1:
        dic[x] = {0:1, 1:1}
        return "1 1"
    else:
        dic[x] = {}
        dic[x][0] = 1
        for num in range(1,len(dic[x-1])):
            dic[x][num] = dic[x-1][num] + dic[x-1][num-1]
        dic[x][x] = 1
        row = ' '.join(str(a) for a in dic[x].values())
        return row

def execute():    
    for x in range(750):   ## modify the number 750 to change the number of rows to find
        row = pascal(x)
        print(row)         ## comment this out to only find the processing time of the code

def average_time(reps):
    timel = []
    for x in range(reps):
        starttime = timeit.default_timer()
        execute()
        instant_time = timeit.default_timer() - starttime
        timel.append(instant_time)
    return sum(timel)/len(timel)

avg = average_time(50)     ## modify the number 50 to change the number of times the code runs (this is mainly to get a reliable average processing time)
print("--------------- Pascal triangle(memoized)---------------")
print("The code finds the first 750 lines of the pascal triangle")
print("The average time of 50 runs of the code is: {}".format(avg))
print("--------------------------------------------------------")
