# 在命令库中抽取五个命令
import random


def main():  # file_os/rest_commder.txt,file_os/text.txt
    with open('/home/cole/Desktop/command_sampling_exercise/text.txt', 'r') as f:
        a = f.readlines()
        b = random.sample(a, 5)
        for i in b:
            print(i, end='')
    print(len(a))
    rest = list(set(a)-set(b))
    rest.sort()
    print(len(rest))
    with open('/home/cole/Desktop/command_sampling_exercise/rest.txt','w+') as f:
        f.writelines(rest)
    with open('command_sampling_exercise/try.py', 'w+') as f:
        f.writelines("'''\n")
        f.writelines(b)
        f.writelines("'''\n")


if __name__ == '__main__':
    main()
