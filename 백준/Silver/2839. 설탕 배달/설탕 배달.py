suggar = int(input())

bag = 0
while suggar >= 0:
    if suggar % 5 == 0:
        bag += suggar // 5
        print(bag)
        break
    suggar -= 3
    bag += 1
else:
    print(-1)