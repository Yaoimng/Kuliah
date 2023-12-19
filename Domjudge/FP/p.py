n = int(input())
numbers = list(map(int, input().split()))

list = []
list.append(numbers)

for i in range (n-1):
    new_list = []
    for j in range (len(numbers) - 1):
        new_list.append(numbers[j + 1] - numbers[j])    
    list.append(new_list)
    numbers = new_list
result = 0
for i in list:
    result += i[-1]

print (result)