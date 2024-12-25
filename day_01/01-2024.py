def lists_from_file(fileName: str):
    list1 = []
    list2 = []
    file = open(fileName, 'r')
    for line in file:
        nums = line.split()
        list1.append(int(nums[0]))
        list2.append(int(nums[1]))
    list1.sort()
    list2.sort()
    return list1, list2

def get_distances(list1, list2):
    dist = 0
    for n1, n2 in zip(list1, list2):
        dist += abs(n1 - n2)
    return dist

def get_similarity_score(list1, list2):
    sim = 0
    for num in list1:
        sim += num * list2.count(num)
    return sim

if __name__ == '__main__':
    list1, list2 = lists_from_file('day_01/input.txt')
    sim = get_similarity_score(list1, list2)
    print('The similarity score between the lists is', sim)
    dist = get_distances(list1, list2)
    print('Distance between the lists: ', dist)
