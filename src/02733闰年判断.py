year = int(input())
result = "N"
if year%4 == 0 :
    result = "Y"
if year%100 == 0 and year%400 != 0 :
    result = "N"
if year%3200 == 0 :
    result = "N"
print(result)
