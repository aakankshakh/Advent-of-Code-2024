import sys

list1 = []
list2 = []

for line in sys.stdin:
    if line.strip() == '':
        break
    two_nums = line.strip().split('   ')
    list1.append(int(two_nums[0]))
    list2.append(int(two_nums[1]))

similarity_score = 0

for num in list1:
    list2_count = list2.count(num)
    similarity_score += num * list2_count

print(similarity_score)
    
