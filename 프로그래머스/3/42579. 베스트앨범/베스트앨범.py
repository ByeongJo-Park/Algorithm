def solution(genres, plays):
    answer = find(genres, plays)
    return answer

def find(g, p):
    dic = dict()
    ans = []
    l = len(g)
    for i in range(l):
        idx = i
        gen = g[i]
        play = p[i]
        if gen in dic:
            dic[gen][0] += play
            dic[gen][1].append((idx, play))
            t = len(dic[gen][1])
            if t >= 2:
                dic[gen][1].sort(key=lambda x: (-x[1], x[0]))
                if t > 2:
                    dic[gen][1].pop()
        else:
            dic[gen] = [play, [(idx, play)]]
    play_list = list(dic.items())
    play_list.sort(key=lambda x : -x[1][0])

    k = len(play_list)
    for j in range(k):

        if len(play_list[j][1][1]) == 1:
            ans.append(play_list[j][1][1][0][0])
        else:
            ans.append(play_list[j][1][1][0][0])
            ans.append(play_list[j][1][1][1][0])
    return ans