# ------------------------------------------------------
# 문제 번호 : [2438] 별 찍기 - 1
# 플랫폼 : Baekjoon
# 링크 : https://www.acmicpc.net/problem/2438
# 난이도 : X
# 분류 : 구현
# 날짜 : 2024-10-29
# ------------------------------------------------------

# 문제 설명 :
# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

# 코드
n = int(input())

for i in range(n):
    print("*" * (i+1))
