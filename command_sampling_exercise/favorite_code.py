# filename=input('')
# 打开随机文件抽取所写的命令行
with open('command_sampling_exercise/try.py', 'r')as f:
    # 逐行写入所读取的命令行
    content = f.readlines()
# 打开收藏命令行的文件
with open('command_sampling_exercise/collection1.py', 'a+')as f:
    # 先打印两个空行，再把命令行打印进文件
    # a+追加模式
    f.writelines("\n")
    f.writelines("\n")
    f.writelines(content)
