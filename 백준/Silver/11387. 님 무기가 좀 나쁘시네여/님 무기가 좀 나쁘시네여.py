slot = []
for i in range(4):
    opts = list(map(int, input().split()))
    slot.append(opts)

def ability(dmg, strengh, cri, cridmg, attspd):
    return dmg * (100 + strengh) * (100 * (100 - min(cri, 100)) + (min(cri, 100) * cridmg)) * (100 + attspd)

check = [
    slot[0],
    slot[1],
    [slot[0][0]-slot[2][0]+slot[3][0], slot[0][1]-slot[2][1]+slot[3][1], slot[0][2]-slot[2][2]+slot[3][2], slot[0][3]-slot[2][3]+slot[3][3], slot[0][4]-slot[2][4]+slot[3][4]],
    [slot[1][0]-slot[3][0]+slot[2][0], slot[1][1]-slot[3][1]+slot[2][1], slot[1][2]-slot[3][2]+slot[2][2], slot[1][3]-slot[3][3]+slot[2][3], slot[1][4]-slot[3][4]+slot[2][4]]
]

print('+' if ability(*check[0]) < ability(*check[2]) else 0 if ability(*check[0]) == ability(*check[2]) else '-')
print('+' if ability(*check[1]) < ability(*check[3]) else 0 if ability(*check[1]) == ability(*check[3]) else '-')