import timeit

def pascal (x):
    if x == 0:
        return [1]
    if x == 1:
        return [1, 1]
    else:
        row = [1]
        above_row = pascal(x-1)
        for num in range(1, len(above_row)):
            row.append(above_row[num] + above_row[num-1])
        row.append(1)
        return row

def execute():
    for x in range(500):   ## modify the number 750 to change the number of rows to find
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
print("------------- Pascal triangle(not memoized)-------------")
print("The code finds the first 500 lines of the pascal triangle")
print("The average time of 50 runs of the code is: {}".format(avg))
print("--------------------------------------------------------")
