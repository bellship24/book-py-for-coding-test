'''
그래프 이론 : 실전 문제 : 4. 커리큘럼

'선수 강의' -> 대체로 위상 정렬.

- 총 N 개의 강의.
- 모든 강의는 1번부터 N번 까지 번호를 갖음.
- 동시에 여러 개의 강의를 들을 수 있음.
- 각 강의는 수강까지 최소 시간이 있음.
- 특정 강의의 수강까지 최소 시간은 선수 강의의 수강까지 최소 시간을 더한 값.

# 위상 정렬 과정
- 진입 차수 list 생성 및 초기화
- 큐 생성
- 진입차수가 0인 간선을 큐에 넣기
- 큐가 빌 때 까지 반복
    - 큐에서 원소 하나 꺼내서 해당 간선에 포함된 노드들에 대한 진입 차수 -1
    - 진입 차수가 0인 노드들을 큐에 넣기
'''

from collections import deque

n = int(input())
lectures = [[] * (n+1)]
times = [0] * (n+1)
indegree = [0] * (n+1)

for i in range(1, n+1):
    lecture = list(map(int, input().split()))
    times[i] = lecture[0]

    for pre in lecture[1:-1]:
        indegree[i] += 1
        lectures[i].append(pre)

q = deque()

for i, v in indegree:
    if v == 0:
        q.append(i)

while q:
    now = q.popleft()

    for pre in lectures[now]:
        times[now] = max(times[now], times[now]+times[pre])
        indegree[pre] -= 1
        if indegree[pre] == 0:
            q.append(pre)

    
for time in times[1:]:
    print(time, end='')

'''
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1



'''