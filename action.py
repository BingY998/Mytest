import os
import subprocess
import sys


# 1.执行cmd命令，不显示执行过程中弹出的黑框
def run_cmd(cmd_str='', echo_print=1):
    """
    执行cmd命令，不显示执行过程中弹出的黑框
    备注：subprocess.run()函数会将本来打印到cmd上的内容打印到python执行界面上，所以避免了出现cmd弹出框的问题
    :param cmd_str: 执行的cmd命令
    :return:
    """
    from subprocess import run
    if echo_print == 1:
        print('执行cmd指令="{}"'.format(cmd_str))
    # shell=True,subprocess.Popen接受字符串类型的变量作为命令，并调用shell去执行这个字符串
    # shell=False,subprocess.Popen只接受数组变量作为命令，并将数组的第一个元素作为命令，剩下的全部作为该命令的参数。
    run(cmd_str.encode(sys.getfilesystemencoding()), shell=True)


# 2.执行cmd命令，并得到执行后的返回值，python调试界面输出返回值
def run_cmd_Popen_fileno(cmd_string):
    """
    执行cmd命令，并得到执行后的返回值，python调试界面输出返回值
    :param cmd_string: cmd命令，如：'adb devices'
    :return:
    """
    import subprocess

    print('运行cmd指令：{}'.format(cmd_string))
    return subprocess.Popen(cmd_string.encode(sys.getfilesystemencoding()), shell=True, stdout=None,
                            stderr=None).wait()  # 等待子进程终止，可以指定超时时间


# 3.执行cmd命令，并得到执行后的返回值,python调试界面不输出返回值
def run_cmd_Popen_PIPE(cmd_string):
    """
    执行cmd命令，并得到执行后的返回值,python调试界面不输出返回值
    :param cmd_string: cmd命令，如：'adb devices"'
    :return:
    """
    import subprocess

    print('运行cmd指令：{}'.format(cmd_string))
    return \
        subprocess.Popen(cmd_string.encode(sys.getfilesystemencoding()), shell=True, stdin=subprocess.PIPE,
                         # shell方法参数为True，将通过操作系统的shell执行指定命令
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE,  ## stdin, stdout, stderr	分别表示程序的标准输入、输出、错误句柄
                         encoding='gb2312').communicate()[0]  # communicate(input,timeout)与子进程交互，发动和读取数据


def ActionFunction1(self):
    print("第1个解模糊成功了！")
    # run_cmd('cd./')
    # run_cmd_Popen_fileno('adb devices')
    # os.startfile(r'D:\Software\Notepad++\notepad++.exe')  # python调用windows下的应用程序
    # os.system('nvidia-smi')

#    os.startfile(r'D:\PyCharm Community Edition 2021.1.3\bin\pycharm64.exe')


#    os.startfile(r'C:\Windows\System32\cmd.exe')  # python调用windows下的应用程序
#    run_cmd_Popen_PIPE('adb devices')


def ActionFunction2(self):
    print("第2个解模糊成功了！")


def ActionFunction3(self):
    print("第3个解模糊成功了！")


def ActionFunction4(self):
    print("第4个解模糊成功了！")


def ActionFunction5(self):
    print("第5个解模糊成功了！")
