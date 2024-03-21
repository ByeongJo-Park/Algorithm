def solution(edges):
    answer = findCreate(edges)
    return answer


edge_1 = [[2, 3], [4, 3], [1, 1], [2, 1]]
edge_2 = [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]

def findCreate(edges):
    l = len(edges)

    s_check = dict()
    e_check = dict()
    create_node = 0
    stick_node = 0
    eight_node = 0
    for i in range(l):
        s, e = edges[i]
        if s in s_check:
            s_check[s].append(e)
        else:
            s_check[s] = [e]

        if e in e_check:
            e_check[e].append(s)
        else:
            e_check[e] = [s]

    for k, v in s_check.items():
        if len(v) > 1 and k not in e_check:
            create_node = k

        if len(v) >= 2 and k in e_check and len(e_check[k]) >= 2:
            eight_node += 1

    for k, v in e_check.items():
        if k not in s_check:
            stick_node += 1

    return [create_node, len(s_check[create_node]) - eight_node - stick_node, stick_node, eight_node]
# 도넛(n) : n / n
# 막대(n) : n / n - 1
# 8자(n) : 2n + 1 / 2n + 2

print(solution(edge_1))
print(solution(edge_2))