# KOI의 컴퓨터 시리얼 넘버 6자리 중 5자리는 00000 ~ 99999 수 중 하나가, 6번쨰는 검증수가 들어간다. 각 자리의 제곱수의 합을 10으로 나눈 값.
"""
    입력 : 첫째 줄에 고유번호의 처음 5자리가 빈칸을 사이에 두고 하나씩 주어짐
    출력 : 첫째 줄에 검증수를 출력
"""
typed = [int(a) for a in input().split()]
total = 0

for a in typed:
    total += (a ** 2)

print(total % 10)