#Working with huge amount of data, Twitter Question University test 7,, 2018
#Time Series Data Aggregation







# Enter your code here. Read input from STDIN. Print output to STDOUT
infotweet = [i for i in input().strip().split(', ')]
info = input()
info = input()
output = {}
while info:
    info = [i for i in info.strip().split(', ')]
    info[2] = int(info[2])
    info[0] = info[0][:-3]
    if infotweet[0] <= info[0] < infotweet[1]:
        if info[0] in output.keys():
            if info[1] in output[info[0]].keys():
                output[info[0]][info[1]] += info[2]
            else:
                output[info[0]][info[1]] = info[2]
        else:
            output[info[0]] = {}
            output[info[0]][info[1]] = info[2]
    try:
        info = input()
    except EOFError:
        info = ""
for i in sorted(output.keys(), reverse = True):
    line = i 
    for j in sorted(output[i].keys()):
        line += ', ' + j + ', ' + str(output[i][j])
    print (line)