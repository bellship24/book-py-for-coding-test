"""
- 분당 3이 포함된 총 개수 (15개)
  - 03, 13, 23, 33, 43, 53  //  30, 31, 32, 34, 35, 36, 37, 38, 39
- 초당 3이 포함된 총 개수 (")
  - "
- 시간당 3이 포함된 총 개수 = 분당 3이 포함된 총 개수 * 초당 3이 포함된 총 개수
  - 15 * 15 = 225
- 주어진 n시까지 3이 포함된 총 개수
  - (n+1) * 시간당 3이 포함된 총 개수
  - (n+1) * 225
  - 단, n이 3보다 크면
    - n * 225 + 59 * 59
    - 59 * 59 란 3시에는 모든 수를 포함하기 때문
        - 59 * 59 = 3481 을 더함
"""