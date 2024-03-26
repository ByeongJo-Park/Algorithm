def solution(gems):
    lg = len(gems)
    answer = [0, lg]
    l, r = 0, 0
    gem_list_size = len(set(gems))
    gem_dict = dict()
    gem_dict[gems[0]] = 1
    while l < lg and r < lg:
        if len(gem_dict) == gem_list_size:
            if r - l < answer[1] - answer[0]:
                answer = [l+1, r+1]
            else:
                gem_dict[gems[l]] -= 1
                if gem_dict[gems[l]] == 0:
                    gem_dict.pop(gems[l])
                l += 1
        else:
            r += 1

            if r == lg:
                break

            if gems[r] in gem_dict:
                gem_dict[gems[r]] += 1
            else:
                gem_dict[gems[r]] = 1

    return answer