n = int(input())
print(n//5 + n//25 + n//125)
# 뒷자리가 0인 나오는 경우는2, 5, 10을 곱할 때
# 그래서 5의 개수를 찾는다(5로 나눠지는 몫을 더해줌)
# n의 범위가 500까지 이므로 125도 넣어준다