# n = int(input())
# answer = []
# for i in range(n):
#     s = int(input())
#     a = int(input())
#     p = list(map(int, input().split()))
#     b = int(input())
#     q = list(map(int, input().split()))
#     ans = 0
#     complement_p = [s-pi for pi in p]
#     set_co_p = set(complement_p)
#     set_q = set(q)
#     common_ele = set_co_p & set_q
#     for ele in common_ele:
#         ans += complement_p.count(ele)*q.count(ele)
#     answer.append(ans)
# for ans in answer:
#     print(ans)
#
# '''在自己的努力下ac，使用set来减小复杂度'''

n = int(input())
answer = []
for _ in range(n):
    s = int(input())
    a = int(input())
    p = list(map(int, input().split()))
    b = int(input())
    q = list(map(int, input().split()))

    # 创建 complement_p 和 q 的频次字典
    complement_p_freq = {}
    for pi in p:
        complement = s - pi
        complement_p_freq[complement] = complement_p_freq.get(complement, 0) + 1

    q_freq = {}
    for qi in q:
        q_freq[qi] = q_freq.get(qi, 0) + 1

    # 计算交集中元素的乘积和
    ans = 0
    for ele in complement_p_freq:
        if ele in q_freq:
            ans += complement_p_freq[ele] * q_freq[ele]

    answer.append(ans)

# 输出答案
for ans in answer:
    print(ans)

'''这是gpt代码，用字典进一步减小了复杂度/不需要count()'''