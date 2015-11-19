def boardify(b):
    return [[int(x) for x in r.split("|") if x]
            for r in b.split("\n") if "+" not in r]

def is_knight((a, b), (x, y)):
    return sorted([abs(a-x), abs(b-y)]) == [1,2]

def find(b, n):
    i = min(x for (x,r) in enumerate(b) if n in r)
    j = b[i].index(n)
    return (i,j)

def check(b):
    return all(is_knight(find(b, n), find(b, n+1)) for n in range(1,64))


with open("closedknightstoursolns.txt") as f:
    s = f.read()

for board in [x for x in s.split("\n\n") if x]:
    try:
        if check(boardify(board)):
            print "Hurrah!"
        else:
            print "WUH OH!"
            break
    except ValueError:
        print "WAAAAAAH!!!"
        break
else:
    print "Come on and slam!"
    print "And welcome to the jam!"
