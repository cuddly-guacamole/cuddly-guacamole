# 导入os模块，用于操作系统相关功能
import os
# 导入sys模块，用于访问与Python解释器相关的变量和函数
import sys

# 定义run_script函数，用于运行指定脚本文件
def run_script(script_name, encoding='utf-8'):
    # 打印正在运行脚本的提示信息
    print(f"Running {script_name}...")
    # 获取脚本的完整路径，基于当前工作目录和脚本名称
    script_path = os.path.join(os.getcwd(), script_name)
    # 检查脚本文件是否存在
    if not os.path.exists(script_path):
        # 如果脚本文件不存在，打印错误信息并退出程序
        print(f"{script_name} not found.")
        sys.exit(1)

    # 检查脚本文件是否不是"__main__.py"，如果不是，则尝试执行脚本文件
    if script_name != "__main__.py":
        try:
            # 读取脚本文件内容并执行
            with open(script_path, 'r', encoding=encoding) as file:
                code = file.read()
            exec(code, globals())
        except Exception as e:
            # 如果执行过程中出现错误，打印错误信息并退出程序
            print(f"Error running {script_name}: {e}")
            sys.exit(1)
        finally:
           # 从运行脚本列表中移除已运行的脚本
           scripts.remove(script_name)
           # 将运行过的脚本添加到列表中
           run_scripts.append(script_name)

# 主程序，获取当前工作目录下的所有文件
if __name__ == "__main__":
    # 获取当前工作目录下的所有文件
    scripts = os.listdir()
    # 创建一个空列表，用于存储已经运行过的脚本
    run_scripts = []
    # 遍历所有文件
    for script in scripts:
        # 如果文件是Python脚本，则运行该脚本
        if script.endswith(".py"):
            run_script(script)
