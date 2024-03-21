def solution(edges):
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