# ------------------------------------------------------
# 문제 번호 : [1330] 두 수 비교하기
# 플랫폼 : Baekjoon
# 링크 : https://www.acmicpc.net/problem/1330
# 난이도 : X
# 분류 : 구현
# 날짜 : 2024-10-29
# ------------------------------------------------------

# 문제 설명 :
# 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.

# 코드
a,b=map(int,input().split())
if a>b :
    print('>')
elif a<b:
    print('<')
else :
    print('==')
