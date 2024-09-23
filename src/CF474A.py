

direction = input()
words = input()
R = {"s":"a", "w":"q", "x":"z", "e":"w", "d":"s", "c":"x",
     "r":"e", "f":"d", "v":"c", "t":"r", "g":"f", "b":"v",
     "y":"t", "h":"g", "n":"b", "u":"y", "j":"h", "m":"n",
     "i":"u", "k":"j", ",":"m", "o":"i", "l":"k", ".":",",
     "p":"o", ";":"l", "/":".", "'":";"}
L = {"q":"w", "a":"s", "z":"x", "w":"e", "s":"d", "x":"c",
     "e":"r", "d":"f", "c":"v", "r":"t", "f":"g", "v":"b",
     "t":"y", "g":"h", "b":"n", "y":"u", "h":"j", "n":"m",
     "u":"i", "j":"k", "m":",", "i":"o", "k":"l", ",":".",
     "o":"p", "l":";", ".":"/"}

mapping = R if direction == "R" else L

trans = "".join(mapping[letter] for letter in words)

print(trans)