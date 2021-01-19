
while True:
    fname = input("Enter file name: ")
    if fname == 'done':
        break
    try:
        fh = open(fname)
        break
    except:
        print('File could now be found')
        continue

lst = list()
wlst = list()

for line in fh:
    w = line.split()
    if w not in lst:
        lst.append(w)
        lst.sort()


for x in lst[0]:
    y = x.split()
    if y not in wlst:
        wlst.append(y)

for x in lst[1]:
    y = x.split()
    if y not in wlst:
        wlst.append(y)

for x in lst[2]:
    y = x.split()
    if y not in wlst:
        wlst.append(y)

for x in lst[3]:
    y = x.split()
    if y not in wlst:
        wlst.append(y)

wlst.sort()
print(wlst)


# for x in lss:
# print(x)

# for x in lst:

# print(wlst)
