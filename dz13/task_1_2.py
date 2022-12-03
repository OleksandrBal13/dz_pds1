import random
import time
from random_words import RandomWords

int_list = []
float_list = []
str_list = []

w = RandomWords()

for i in range(0, 5000):
    int_list.append(random.randint(0, 1000))
    float_list.append(random.uniform(0.1, 100.0))
    str_list.append(w.random_word())

def new_sort(inputdata, num):
    time_list = []
    for i in range(0, int(num)):
        cur_time1 = time.time()
        data1 = list(inputdata)
        data = data1.copy()
        print("Source list: ", data)
        length = len(data)
        for iIndex in range(length):
            swapped = False
            for jIndex in range(0, length - iIndex - 1):
                if data[jIndex] > data[jIndex + 1]:
                    data[jIndex], data[jIndex + 1] = data[jIndex + 1], data[jIndex]
                    swapped = True
            if not swapped:
                break
        print("Bubble Sort: ", data)
        print(f"Duration time: {time.time() - cur_time1}")
        time_list.append(time.time() - cur_time1)
    print(f"Time list: {time_list}")
    print(f"Total time: {sum(time_list)}")
    print(f"Average: {sum(time_list) / len(time_list)}")


new_sort(int_list,10)