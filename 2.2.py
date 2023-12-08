f = open("in.txt", "r")
data = [x.strip() for x in f.readlines()]

colors = [('red',12), ('green',13), ('blue',14)]

id = 1

ans = 0

for l in data:
    _, s = l.split(': ')
    sets = s.split('; ')
    
    flagged = 0
    
    m = {
        'red' : 0,
        'green' : 0,
        'blue' : 0
    }
    
    for s in sets:
        items = s.split(', ')
        for item in items:
            count, color = item.split(' ')         
            m[color] = max(m[color], int(count))

    mul = m['red'] * m['green'] * m['blue']
    ans += mul
    print(mul)
print(ans)
    
                
        