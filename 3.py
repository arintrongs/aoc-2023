f = open("in.txt", "r")
data = [x.strip() for x in f.readlines()]

p = 0


for i in range(len(data)):
    s = data[i]
    print(s.split('.'))   

                
                
    