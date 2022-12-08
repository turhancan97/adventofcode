from collections import defaultdict

data = open('filesystem.txt').read().strip() 
lines = [x for x in data.split('\n')]

# directory path -> total size of that directory (including subdirectories)
SZ = defaultdict(int)
path = [] # current directory path
for line in lines: # for each line in the filesystem
    words = line.strip().split()
    if words[1] == 'cd': 
        if words[2] == '..': 
            path.pop() # remove the last directory from the path
        else:
            path.append(words[2])
    elif words[1] == 'ls': 
        continue # ignore this line
    elif words[0] == 'dir':
        continue # ignore this line
    else:
        sz = int(words[0]) 
        # Add this file's size to the current directory size *and* the size of all parents
        for i in range(1, len(path)+1):
            SZ['/'.join(path[:i])] += sz

max_used = 70000000 - 30000000
total_used = SZ['/']
need_to_free = total_used - max_used

p1 = 0
p2 = 1e9
for k,v in SZ.items():
    #print(k,v)
    if v <= 100000:
        p1 += v
    if v>=need_to_free:
        p2 = min(p2, v)
print(p1)
print(p2)