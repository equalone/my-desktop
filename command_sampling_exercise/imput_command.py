newcommder = input('请输入新命令....:')


def main():
    with open('command_sampling_exercise/text.txt', 'a+', encoding='utf-8') as f:
        f.write('\n'+newcommder)


if __name__ == '__main__':
    main()
