#Prisoners dilemma by veritasium
import random
import time
start = time.time()
op_list = []
for i in range(100000):
    rand_set = set()
    number_list = []
    while len(number_list) != 100:
        number = random.randint(1,100)
        if number not in rand_set:
            number_list.append(number)
            rand_set.add(number)
    number_list = tuple(number_list)
    for prisoner in range(1, 101):
        iter = 50
        index = prisoner
        flag = True
        while iter != 0:
            val = number_list[index - 1]
            index = val
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
print(op_list.count(1)) # average success 31.26%
end= time.time()
print(end - start)