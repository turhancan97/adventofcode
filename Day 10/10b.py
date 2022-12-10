with open('instructions.txt', 'r', encoding="utf-8") as f: # Open the file
    lines = f.readlines() # Read the lines of the file
    lines = [line.strip() for line in lines] # Remove the newline character from each line
    
G = [['?' for _ in range(40)] for _ in range(6)]
ans = 0
x = 1
cycle = 0
cycle_list = list(range(20,221,40))

def handle_tick(cycle, x):
    '''It takes the current cycle and the current position of the cart, and updates the global variable `G`
    to reflect the current state of the track
    
    Parameters
    ----------
    cycle
        the current cycle number
    x
        the current position of the cart
    
    '''
    global ans
    global G
    t1 = cycle-1
    G[t1//40][t1%40] = ('#' if abs(x-(t1%40))<=1 else ' ')
    if cycle in cycle_list:
        ans += x*cycle

for line in lines:
    if line == 'noop':
        cycle += 1
        handle_tick(cycle,x)
    else:
        ins, value = line.split(" ")
        cycle += 1
        handle_tick(cycle,x)
        cycle += 1
        handle_tick(cycle,x)
        x += int(value)
        
print(ans)
for r in range(6):
    print(''.join(G[r]))