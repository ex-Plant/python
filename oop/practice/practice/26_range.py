# Start from 1, with each iteration increase by 1 until you reach max than start decreasing by 1 until you get to 1.

def countReps(max): 
    count = 0;
    for i in range(0, max):
        print(i, 'index')
        if i <= max:
            count += i + 1
    # print(count, 'count_1')

    for i in range(max, 0, -1):
        if i < max:
            print(i, 'sec_index')
            count += i
    
    # print(count, 'count_2')
    return count

print(countReps(7))


def better_count_reps(max):
    count = max
    for i in range(0, max):
        if i < max:
            count += i * 2
    return count

print(countReps(7))
print(better_count_reps(7))
