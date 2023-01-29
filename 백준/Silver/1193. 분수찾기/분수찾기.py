input_n = int(input())
line = 0 
max_n = 0  
while input_n > max_n:
    line += 1  
    max_n += line  

gap = max_n - input_n 
if line % 2 == 0:  
    top = line - gap  
    under = gap + 1  
else :  
    top = gap + 1  
    under = line - gap  
print(f'{top}/{under}')
