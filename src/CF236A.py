name = input()
distinct_letters = []
for char in name :
    if not(char in distinct_letters) :
        distinct_letters.append(char)
length = len(distinct_letters)
if length%2 == 0 :
    print("CHAT WITH HER!")
else :
    print("IGNORE HIM!")