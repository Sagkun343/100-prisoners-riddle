import random
import time


def prisoners_dilemma(iteration_count: int, chances: int, prisoner_number: int):
    flag = bool()
    start = time.time()
    res = 0
    for i in range(iteration_count):
        rand_set = set()
        number_list = []
        while len(number_list) != prisoner_number:  # assigns a random integer to each index pos
            number = random.choice([i for i in range(1, prisoner_number+1) if i not in rand_set])
            number_list.append(number)
            rand_set.add(number)
        number_list = tuple(number_list)
        for prisoner in range(1, prisoner_number + 1):  # iterates and checks if the prisoner is lucky enough
            iteration = chances
            index = prisoner
            flag = True
            while iteration != 0:
                number_set = set()
                val = number_list[index - 1]
                index = val
                if val in number_set:  # edge-case where the prisoner know they're on a loop
                    rand = random.choice([i for i in range(1, prisoner_number+1) if i not in number_set])
                    index = rand
                else:
                    number_set.add(val)
                if index == prisoner:
                    break
                else:
                    iteration -= 1
                if iteration == 0:
                    flag = False
            if flag is False:
                break
        if flag is True:
            res += 1
    success_percentage = (res / iteration_count) * 100
    print(f"success percentage = {success_percentage}%")  # increased average success%, now at 31.42%
    end = time.time()
    print(f"time taken:{end - start}")
    return None


if __name__ == "__main__":
    prisoners_dilemma(100000, 50, 100)
