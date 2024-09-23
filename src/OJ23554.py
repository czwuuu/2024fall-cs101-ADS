n = int(input())
numbers = list(map(int, input().split()))
our_class = [number for number in numbers if number <= n]
other_class = [number for number in numbers if number > n]
other_class.sort()
full = list(range(1, n+1))
lost = [child for child in full if child not in numbers]
print(" ".join(map(str, lost)))
print(" ".join(map(str, other_class)))
