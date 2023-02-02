n = int(input())
move_plan_list = input().split()

place = [1, 1]

while move_plan_list:
    arrow = move_plan_list.pop(0)
    
    if arrow == "R":
        if place[1] < n:
            place[1] += 1
    elif arrow == "L":
        if place[1] > 1:
            place[1] -= 1
    elif arrow == "U":
        if place[0] > 1:
            place[0] -= 1
    elif arrow == "D":
        if place[0] < n:
            place[0] += 1
    
print(place)


'''
5
R R R U D D
[3, 4]
'''