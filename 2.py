f = open("in.txt", "r")
data = [x.strip() for x in f.readlines()]

colors = [('red',12), ('green',13), ('blue',14)]

id = 1

ans = 0

for l in data:
    _, s = l.split(': ')
    sets = s.split('; ')
    
    flagged = 0
    for s in sets:
        items = s.split(', ')
        for item in items:
            for c in colors:
                color, limit = c
                if color in item:
                    count = int(item.split(' ')[0])
                    if count > limit:
                        flagged = 1
                        break
            if flagged == 1:
                break
    
    if flagged == 0:
        ans += id
        # print('===', id)
    id += 1

print(ans)
    
                
        