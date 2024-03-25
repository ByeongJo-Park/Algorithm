from itertools import permutations

def solution(user_id, banned_id):
    answer = []
    bl = len(banned_id)
    user_comb = list(permutations(user_id, bl))
    comb_l = len(user_comb)
    for i in range(comb_l):
        ans_comb = []
        for j in range(bl):
            uw = user_comb[i][j]
            bw = banned_id[j]
            uwl = len(uw)
            bwl = len(bw)
            if uwl != bwl:
                break
            else:
                t = True
                for k in range(uwl):
                    if uw[k] == bw[k]:
                        continue
                    elif bw[k] == '*':
                        continue
                    elif bw[k] != '*' and uw[k] != bw[k]:
                        t = False
                        break
                if t == True:
                    ans_comb.append(uw)
        if len(ans_comb) == bl:
            ans_comb.sort()
            if ans_comb in answer:
                continue
            else:
                answer.append(ans_comb)
    return len(answer)