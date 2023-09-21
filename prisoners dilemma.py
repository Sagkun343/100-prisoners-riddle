import random
import time
start = time.time()
op_list = []
iteration_count = 100000
for i in range(iteration_count):
    rand_set = set()
    number_list = []
    prisoner_number = 100
    while len(number_list) != prisoner_number:#assigns a random integer to each index pos
        number = random.randint(1, prisoner_number)
        if number not in rand_set:
            number_list.append(number)
            rand_set.add(number)
    number_list = tuple(number_list)
    for prisoner in range(1, prisoner_number + 1):# iterates and checks if the prisoner is lucky enough
        iter = 50
        index = prisoner
        flag = True
        while iter != 0:
            number_set = set()
            val = number_list[index - 1]
            index = val
            if val in number_set:
                while True: #edge-case where the prisoner knows they're on a loop but has not run out of iterations
                    rand = random.randint(1, prisoner_number)
                    if rand not in number_set:
                        index = rand
                        break
            else:
                number_set.add(val)
            if index == prisoner:
                break
            else:
                iter -= 1
            if iter == 0:
                flag = False
        if flag is False:
            op_list.append(0)
            break
    if flag is True:
        op_list.append(1)
success_percentage = (op_list.count(1) / iteration_count) * 100
print(f"success chance = {success_percentage}%")# increased average success%, now at 31.42%
end= time.time()
print(f"time taken:{end - start}")