try: 
    number = int(input("Number: "))
except: 
    print("Enter a number!")

lst = list(str(number)) 

len = len(lst)
if len < 13 or len > 16: 
    print("INVALID")

sum = 0 
for i in lst[::2]:
    product = int(i) * 2
    if product >= 10: 
        product = list(str(product))
        sum += int(product[0]) + int(product[1])
    else: 
        sum += product  

for j in lst[1::2]: 
    sum += int(j) 

if sum % 10 == 0: 
    first_2 = int(str(number)[:2])
    print(first_2)
    if first_2 == 34 or first_2 == 37: 
        print("American Express")
    if first_2 >= 51 and first_2 <= 55: 
        print("MasterCard")
    elif first_2 >= 40 and first_2 < 50: 
        print("Visa")  

print("sum", sum)