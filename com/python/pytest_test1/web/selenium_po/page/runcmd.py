"""
用python执行cmd命定
---------------------------------------------------------------------------------------------------------------------
方法	             |    解释
---------------------------------------------------------------------------------------------------------------------
os.system(cmd)	     |os.system()无法获取控制台输出的内容，只是简单的执行cmd指令，返回命令退出状态，其中结果为0表示执行成功
os.popen(cmd).read() |os.popen()可以获取控制台输出的内容，返回的是一个file对象
subprocess.Popen(cmd)|功能更高级，强大subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
---------------------------------------------------------------------------------------------------------------------
eg: 执行cmd命令查看python版本号python -V
"""
# from imp import reload
# from importlib import reload

import commands
import os
import subprocess
import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

class TestPythonCMD:
    """python运行CMD命令"""

    def runcmd(self):
        """用cmd命令启用chrome浏览器默认端口"""
        # print("os执行的命令：",os.system("python"))
        # print("os.open执行的命令：",os.popen("python -V").read())
        # print("subprocess.Popen执行的命令：",subprocess.Popen("python"))
        # print(os.system('ping https://www.baidu.com/'))

        cmd1 = r"cd C:\Program Files (x86)\Google\Chrome\Application"
        cmd2 = "chrome --remote-debugging-port=9222"
        cmd  = cmd1 + "&&" + cmd2

        subprocess.Popen(cmd,shell=True)

# if __name__ == '__main__':
