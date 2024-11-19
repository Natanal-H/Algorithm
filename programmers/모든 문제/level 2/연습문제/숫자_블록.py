# 프로그래머스 문제 풀이 - 숫자 블록 (12923)

## 문제 정보
# **문제 이름**: 숫자 블록
# **문제 번호**: 12923
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/12923)
# **풀이 날짜** : 2024-11-19

## 문제 
# 문제 설명 :
# 그렙시에는 숫자 0이 적힌 블록들이 설치된 도로에 다른 숫자가 적힌 블록들을 설치하기로 하였습니다. 숫자 블록을 설치하는 규칙은 다음과 같습니다.
# 블록에 적힌 번호가 n 일 때, 가장 첫 블록은 n * 2번째 위치에 설치합니다. 그 다음은 n * 3, 그 다음은 n * 4, ...위치에 설치합니다. 기존에 설치된 블록은 빼고 새로운 블록을 집어넣습니다.
# 블록은 1이 적힌 블록부터 숫자를 1씩 증가시키며 순서대로 설치합니다. 예를 들어 1이 적힌 블록은 2, 3, 4, 5, ... 인 위치에 우선 설치합니다. 
# 그 다음 2가 적힌 블록은 4, 6, 8, 10, ... 인 위치에 설치하고, 3이 적힌 블록은 6, 9, 12... 인 위치에 설치합니다.
#
# 그렙시는 길이가 1,000,000,000인 도로에 1부터 10,000,000까지의 숫자가 적힌 블록들을 이용해 위의 규칙대로 모두 설치 했습니다. 그렙시의 시장님은 특정 구간에 어떤 블록이 깔려 있는지 알고 싶습니다.
# 구간을 나타내는 두 정수 begin, end 가 매개변수로 주어 질 때, 그 구간에 깔려 있는 블록의 숫자 배열을 return하는 solution 함수를 완성해 주세요.

## 코드
def solution(begin, end):
    arr = [1] * (end - begin + 1)
    
    for i in range(begin, end+1):
        index = i - begin
        if i == 0 or i == 1 : arr[index] = 0
        else :
            for j in range(2, int(i**0.5)+1):
                if i % j == 0:
                    if i // j > 1e7 : 
                        arr[index] = j
                        continue
                    arr[index] = (i//j)
                    break
    
    return arr
