# 링크
# https://www.acmicpc.net/problem/5218

# 알파벳 거리

# 문제
# 길이가 같은 두 단어가 주어졌을 때, 각 단어에 포함된 모든 글자의 알파벳 거리를 구하는 프로그램을 작성하시오.

# 두 글자 x와 y 사이의 알파벳 거리를 구하려면, 먼저 각 알파벳에 숫자를 할당해야 한다. 'A'=1, 'B' = 2, ..., 'Z' = 26. 그 다음 y ≥ x인 경우에는 y-x, y < x인 경우에는 (y+26) - x가 알파벳 거리가 된다.

# 예를 들어, 'B'와 'D' 사이의 거리는 4 - 2 = 2이고, 'D'와 'B' 사이의 거리는 (2+26) - 4 = 24이다.

# 입력
# 첫째 줄에 테스트 케이스의 수 (< 100)가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 두 단어가 공백으로 구분되어져 있다. 단어의 길이는 4보다 크거나 같고, 20보다 작거나 같으며, 알파벳 대문자로만 이루어져 있다.

# 출력
# 각 테스트 케이스 마다 각 글자의 알파벳 거리를 공백으로 구분해 출력한다.

# 출력 형식
# 정확한 출력 형식은 제출에서 언어를 Java로 설정하면 확인할 수 있다.

# 예제 입력 1
# 5
# AAAA ABCD
# ABCD AAAA
# DARK LOKI
# STRONG THANOS
# DEADLY ULTIMO
# 예제 출력 1
# Distances: 0 1 2 3
# Distances: 0 25 24 23
# Distances: 8 14 19 24
# Distances: 1 14 9 25 1 12
# Distances: 17 7 19 5 1 16

# 함수 -----------------------------------------------------------
def solution():
    T = int(input())
    for i in range(T):
        word1, word2 = input().split()
        resultList = []
        for j in range(len(word1)):
            if(word2[j] >= word1[j]):
                resultList.append(ord(word2[j])-ord(word1[j]))
            else:
                resultList.append(ord(word2[j])-ord(word1[j])+26)
        print("Distances:", *resultList)


# 실행 ------------------------------------------------------------
solution()