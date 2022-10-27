x = {}
x[1] = 1
x['1'] = 2
x[1]=x[1]+1

count = 0
for f in x:
    count +=x[f]
print(count)
