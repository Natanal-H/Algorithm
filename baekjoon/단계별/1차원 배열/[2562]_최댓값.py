# ------------------------------------------------------
# 문제 번호 : [2562] 최댓값
# 플랫폼 : Baekjoon
# 링크 : https://www.acmicpc.net/problem/2562
# 난이도 : X
# 분류 : 구현
# 날짜 : 2024-10-30
# ------------------------------------------------------

# 문제 설명 :
# 9개의 서로 다른 자연수가 주어질 때, 
# 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

# 코드
m, k = 0, 0

for i in range(9):
    n = int(input())
    if  m < n :
        m = n
        k = i + 1
        
print(m)
print(k)
