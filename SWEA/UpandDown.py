# *주의 : 난이도를 매우 올려둔 문제입니다. 문제를 관성적으로 풀지 않도록 주의하세요.

# 어느날 교수님은 문득 OO산 등반을 하고 싶었다.
# 그래서 조교A에게 같이 산에 올라가자고 제안하였다.


# 조교는 한숨을 푹 쉬며, N*N 공간의 주변 일대에 산 정상의 높이가
# 가장 높은 산과 가장 낮은 산의 높이차를 파악해보기로 하였다.

# *제약조건
# 1. 한 구역을 중심으로 8방으로 높으면 산의 정상이다.
# 2. 단, 가장자리는 산의 정상으로 취급하지 않는다.
# 3. 산이 하나 이하인 경우에는 수행하지 않는다.
 

# [입력]
 

# 첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 10 )

# 다음 줄부터 테스트케이스의  정수 개수 N이 주어진다 ( 3 ≤ N ≤ 100 )

# 다음 줄에 N개의 높이 값 a1가 공백과 함께 주어진다 ( 0 ≤ a1 ≤ 300 ) 

 

# [출력]
 

# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 산의 높이차를 순서대로 출력하시오.
# (*산이 하나만 있거나 없는 경우에는 -1을 출력하시오.)
'''
4
3
1 2 3
4 5 3
4 1 2
4
1 1 1 1
1 5 1 1
1 1 6 1
1 1 1 1
5
1 1 1 1 1
1 5 1 1 1
1 1 1 5 1
1 1 1 1 1
1 1 1 1 1
5
1 1 1 1 1
1 6 1 3 1
1 1 1 1 1
1 1 1 2 1
1 1 1 1 1
'''

'''
(1) 스택(stack)에 대해 간단히 설명하시오.
- 물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료구조로 선형 구조를 갖고, 후입선출이다.
- 마지막 삽입된 원소의 위치를 top이라 부름.
- 연산으로는 삽입, 삭제, isEmpty. Peek가 있다.
(2) Depth First Search(DFS, 깊이우선탐색)에 대해 간단히 설명하시오.
- 비선형구조인 그래프 구조에서 모든 자료를 빠짐없이 검색하는 방법중 하나로
 시작정점의 한 방향으로 갈수 있는 경로가 있는 곳 까지 깊이 탐색해 가다가 더이상
   갈곳이 없게되면 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아와서
     다른 방향의 정점으로 탐색을 계속반복하여 결국 모든 정점을 방문 순회하는 방법으로 스택을 사용함.

(3) 다음과 같은 그래프에서 4번 정점부터 DFS 를 시작하는 경우의 방문 순서를 적고,
어떤 절차로 탐색을 했는지 간단히 설명하시오.
4-2-1-3-7-6-5
'''