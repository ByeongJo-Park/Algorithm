N, P = map(int, input().split())
W, L, G = map(int, input().split())

winner = set()
player_list = []
cnt, point = 0, 0
done = False
for i in range(P):
    player, info = input().rstrip().split()
    if info == "W":
        winner.add(player)

for _ in range(N):
    player_list.append(input().rstrip())

while cnt < N:
    if point >= G:
        done = True
        break

    if player_list[cnt] in winner:
        point += W
    else:
        point = max(0, point-L)
        
    cnt += 1


print("I AM NOT IRONMAN!!" if done else "I AM IRONMAN!!")