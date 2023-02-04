"""
- 초 단위 모든 시각에 대한 경우의 수는 24 * 60 * 60 = 86400 가지이므로
  100,000개도 되지 않아서 완전 탐색으로 시간 제한 2초 안에 풀 수 있음. 즉, 3중 반복문으로 풀 수 있음.
- 하지만 완전탐색의 경우, 비효율적인 시간 복잡도를  갖고 잇으므로 데이터 개수가 큰 경우 정상적인 동작이 안될 수 있음.
  그러므로 전체 데이터 개수가 100만 개 이하인지 확인해야 함.
- 완전 탐색 방법으로 이 문제를 풀기 위해 1초씩 늘리며 시간을 문자열로 바꿔 3이 포함되어 있는지 체크하자.
"""

# h를 입력받기
h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)

"""
보통 구현 유형과 그리디 유형은 비슷하며 함께 포한된 형태로 출제됨.
"""