import sys
from collections import deque
inp = sys.stdin.readline
N = int(inp())
Card = deque(i + 1 for i in range(N))
while len(Card) > 1:
    Card.popleft()
    Card.append(Card.popleft())

print(Card[0])