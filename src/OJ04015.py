rep = []
while True:
    try:
        address = input()
        check = True
        if address.count("@") != 1:
            check = False
        else:
            local, domain = address.split("@")
            if not local or not domain or local[0] == "." or local[-1] == "." or domain[0] == "." or domain[-1] == ".":
                check = False
            elif "." not in domain:
                check = False

        if check:
            rep.append("YES")
        else:
            rep.append("NO")

    except EOFError:
        break

for ans in rep:
    print(ans)