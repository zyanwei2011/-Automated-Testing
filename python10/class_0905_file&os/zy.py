

with open('test.txt') as f:
    r = f.readlines()
    l = []
    for i in r:
        dict = {}
        r1 = i.strip('\n').split('@')
        for j in r1:
            r2 =j.split(':',1)
            dict[r2[0]] = r2[1]
        l.append(dict)
    print(l)

s = f.closed
print(s)


