# ------------------------------------------------------
# 문제 번호 : [3009] 네번째 점
# 플랫폼 : Baekjoon
# 링크 : https://www.acmicpc.net/problem/3009
# 난이도 : X
# 분류 : 구현, 기하학
# 날짜 : 2024-11-04
# ------------------------------------------------------

# 문제 설명 :
# 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.

# 문제 풀이 :
# 축에 평행한 직사각형이므로, 세 점의 x, y 좌표를 각각 비교해 다른 하나 값을 찾는다

# 코드
arr = [list(map(int, input().split()))
       for i in range(3)]

ans = [0, 0]

for i in range(2):
    for j in range(3):
        if arr[j][i] == arr[(j+1)%3][i]:
            ans[i] = arr[(j+2)%3][i]

print(ans[0], ans[1])
