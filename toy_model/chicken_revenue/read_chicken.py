
with open ('chicken.txt','r') as f:
    lines = f.readlines()

with open('chicken.txt', 'r') as f:
    total_sales=0
    for line in f:
        day_and_sale = line.split()
        total_sales+=int(day_and_sale[1])

print(total_sales / len(lines) )