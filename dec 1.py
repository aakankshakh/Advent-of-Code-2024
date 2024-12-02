import sys

list1 = []
list2 = []

for line in sys.stdin:
    if line.strip() == '':
        break
    two_nums = line.strip().split('   ')
    list1.append(int(two_nums[0]))
    list2.append(int(two_nums[1]))

list1.sort()
list2.sort()

total_distance = 0

for i in range(len(list1)):
    total_distance += abs(list1[i] - list2[i])

print(total_distance)
