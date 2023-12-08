import re

f = open("in.txt", "r")
data = [x.strip() for x in f.readlines()]

ans = 0


value_map = {
    '1,one': 1,
    '2,two' : 2,
    '3,three': 3,
    '4,four': 4,
    '5,five': 5,
    '6,six': 6,
    '7,seven':7,
    '8,eight':8,
    '9,nine':9

}

ii = 0



for l in data:
    mn = 9999
    mx = -1
    
    mn_val = 0
    mx_val = 0
    
    for key,value in value_map.items():
        idx = -1
        
        a,b = key.split(',')

        idx_as = [m.start() for m in re.finditer(a, l)]
        idx_bs = [m.start() for m in re.finditer(b, l)]
        
        idxs = idx_as + idx_bs
        print(idxs)
        idxs.sort()
        
        if len(idxs) > 0:
            
            if idxs[0] < mn:
                mn = idxs[0]
                mn_val = value
            if idxs[-1] > mx:
                mx = idxs[-1]
                mx_val = value
    
    print(int(str(mn_val)+str(mx_val)),ii)
    ii+=1
    if mx_val == 0:
        ans += mn_val
    else:
        ans += int(str(mn_val)+str(mx_val))
        
print(ans)