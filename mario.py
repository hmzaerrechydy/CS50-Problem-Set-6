height = 0

while height <= 0: 
    height = int(input("Height: ")) 

count = 1 

for x in range(height): 
    for s in range(height - count): 
        print(" ", end="")
    
    for y in range(count): 
        print("#", end="")
    
    print("  ", end="")
        
    for h in range(count): 
        print("#", end="")
        
    count += 1
    print()
    