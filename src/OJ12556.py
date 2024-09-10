def run_length_encoding(s):
    s = s.lower()
    if not s:
        return ""

    result = []
    char = s[0]
    num = 1

    for i in range(1, len(s)):
        if s[i] == char:
            num += 1
        else:
            result.append(f"({char},{num})")
            char = s[i]
            num = 1

    # 处理最后一个字符
    result.append(f"({char},{num})")

    return "".join(result)

text = input()
print(run_length_encoding(text))
