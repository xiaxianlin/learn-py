import csv
import random

with open("./res/scores.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["姓名", "语文", "数学", "英语"])
    names = ["关羽", "张飞", "赵云", "马超", "黄忠"]
    for name in names:
        scores = [random.randrange(50, 101) for _ in range(3)]
        scores.insert(0, name)
        writer.writerow(scores)


with open("./res/scores.csv", "r") as file:
    reader = csv.reader(file, delimiter="|")
    for data_list in reader:
        print(reader.line_num, end="\t")
        for elem in data_list:
            print(elem, end="\t")
        print()
