lucky_numbers = [4,7,44,47,74,77,444,447,474,744,477,747,774,777]
n = int(input())
almost_lucky = "NO"
for lucky_number in lucky_numbers:
    if n % lucky_number == 0:
        almost_lucky = "YES"
print(almost_lucky)