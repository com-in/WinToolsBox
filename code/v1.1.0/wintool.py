import os
# from mcstatus import JavaServer

# 严禁格式化本代码
# Do not format this code
# 使用LGPL v2.1开源
# Use LGPL v2.1 open source
# © 2025 Copyright Alice_Ctoy. All rights reserved

# 定义工具箱变量
fix_disk = ""
delete_file = ""
format_disk = ""
set_choice = ""
word_color_choice = ""
bg_color_choice = ""
address = ""

# 定义字典
# ANSI颜色代码映射
COLOR_CODES = {
    '0': '\033[30m',    # 黑色
    '1': '\033[34m',    # 深蓝
    '2': '\033[32m',    # 深绿
    '3': '\033[36m',    # 湖蓝
    '4': '\033[31m',    # 深红
    '5': '\033[35m',    # 紫色
    '6': '\033[33m',    # 金色
    '7': '\033[37m',    # 灰色
    '8': '\033[90m',    # 深灰
    '9': '\033[94m',    # 蓝色
    'a': '\033[92m',    # 绿色
    'b': '\033[96m',    # 天蓝
    'c': '\033[91m',    # 红色
    'd': '\033[95m',    # 粉红
    'e': '\033[93m',    # 黄色
    'f': '\033[97m',    # 白色
    'l': '\033[1m',     # 粗体
    'n': '\033[4m',     # 下划线
    'o': '\033[3m',     # 斜体
    'r': '\033[0m',     # 重置
}

# 定义函数

# 定义主界面
def main_page():
    print("========Windows Tools Box Version 1.0.0=============")
    print("        [1]磁盘修复            [2]文件删除             ")
    print("        [3]格式化              [4]网络连通性测试        ")
    print("        [5]任务管理器          [6]Minecraft服务器查询   ")
    print("        [7]系统信息                                    ") 
    print("        [A]关于")
    print("        [S]设置               ")
    print("        [B]退出               ")
    print("====================================================")

# 定义查询MC服务器
# 格式化motd
def format_motd(motd):
    result = []
    i = 0
    while i < len(motd):
        if motd[i] == '§' and i+1 < len(motd):
            code = motd[i+1].lower()
            # 处理RGB颜色代码 (§x§r§r§g§g§b§b)
            if code == 'x' and i+8 <= len(motd):
                try:
                    r = int(motd[i+2] + motd[i+3], 16)
                    g = int(motd[i+4] + motd[i+5], 16)
                    b = int(motd[i+6] + motd[i+7], 16)
                    result.append(f'\033[38;2;{r};{g};{b}m')
                    i += 8
                    continue
                except (ValueError, IndexError):
                    pass
            # 处理普通格式代码
            result.append(COLOR_CODES.get(code, ''))
            i += 2
        else:
            result.append(motd[i])
            i += 1
    return ''.join(result) + '\033[0m'

# 查询MC服务器
def query_minecraft_server():
    os.system("cls")
    server_address = input("请输入 Minecraft 服务器地址（格式：IP:端口，如未指定端口，默认使用 25565）：")
    if ':' not in server_address:
        server_address = f"{server_address}:25565"
    try:
        server = JavaServer.lookup(server_address)
        status = server.status()
        print(f"服务器在线状态：在线")
        print(f"在线人数：{status.players.online}")
        version_name = status.version.name.lower()
        
        # 判断服务器类型
        server_type_mapping = {
            "mohist": "Mohist",
            "banner": "Banner",
            "purpur": "Purpur",
            "forge": "Forge",
            "neoforge": "NeoForge",
            "fabric": "Fabric",
            "paper": "Paper",
            "spigot": "Spigot"
        }
        
        server_type = "其它"
        for key in server_type_mapping:
            if key in version_name:
                server_type = server_type_mapping[key]
                break
        
        print(f"服务端类型：{server_type}")
        print(f"""Motd：
              {format_motd(str(status.description))}
              """)  # 转换MOTD颜色
    except Exception as e:
        print(f"查询失败，错误信息：{e}")
    os.system("pause")
# 定义磁盘修复
def fix_disk_founction():
    global fix_disk
    fix_disk = input("输入盘符：")
    if len(fix_disk) == 2:
        print("开始修复...")
        os.system(f"chkdsk {fix_disk} /F")
        print("修复完成！")
        os.system("pause")
    elif len(fix_disk) == 1:
        print("开始修复...")
        os.system(f"chkdsk {fix_disk}: /F")
        print("修复完成！")
        os.system("pause")
    else:
        print("啊哦...不是正确的盘符哦")
        os.system("pause")


# 定义文件删除
def file_del():
    global delete_file
    delete_file = input("输入文件夹或文件路径：")
    if os.path.exists(delete_file):
        print("开始删除...")
        os.system(f"del /f /s /q {delete_file}")
        print("删除完成！")
        os.system("pause")
    else:
        print("啊哦...路径不存在哦")
        os.system("pause")

# 定义格式化
def format_disk_founction():
    global format_disk
    format_disk = input("输入盘符：")
    if len(format_disk) == 2:
        print("开始格式化...")
        os.system(f"format {format_disk}")
        print("格式化完成！")
        os.system("pause")
    elif len(format_disk) == 1:
        print("开始格式化...")
        os.system(f"format {format_disk}:")
        print("格式化完成！")
        os.system("pause")
    else:
        print("啊哦...不是正确的盘符哦")
        os.system("pause")
    os.system("pause")

# 定义网络连通性测试
def network_test():
    global address  
    address = input("请输入地址：")
    os.system(f"ping {address}")
    os.system("pause")

# 定义任务管理器
def task_manager():
    os.system("taskmgr")


# 定义设置
def setting():
    global set_choice
    os.system("cls")
    print("=======设置=======")
    print("   [1]字符颜色")
    print("")
    print("   [B]返回主菜单")
    print("=================")
    set_choice = input("请输入选项：")
    if set_choice == "1":
        set_color()
    elif set_choice == "B" or set_choice == "b":
        main_page()
    else:
        print("啊哦...不是正确的选项哦")
        os.system("pause")
        os.system("cls")
        setting()

# 定义字符颜色
def set_color():
    global word_color_choice
    os.system("cls")
    print("""=========对应表=========
        0 = 黑色       8 = 灰色
        1 = 蓝色       9 = 淡蓝色
        2 = 绿色       A = 淡绿色
        3 = 浅绿色     B = 淡浅绿色
        4 = 红色       C = 淡红色
        5 = 紫色       D = 淡紫色
        6 = 黄色       E = 淡黄色
        7 = 白色       F = 亮白色
        """)
    word_color_choice = input("请输入颜色：")
    os.system(f"color {word_color_choice}")
    os.system("cls")
    setting()

def system_info():
    os.system("cls")
    os.system("systeminfo")
    os.system("pause")

while True:
    os.system("cls")
    main_page()
    choice = input("请输入选项：")
    if choice == "1":
        fix_disk_founction()
    elif choice == "2":
        file_del()
    elif choice == "3":
        format_disk_founction()
    elif choice == "4":
        network_test()
    elif choice == "5":
        task_manager()
    elif choice == "6":
        query_minecraft_server()
    elif choice == "7":
        system_info()
    # ↑：功能
    # ↓：自带
    elif choice == "A" or choice == "a":
        os.system("cls")
        print("Windows Tools Box")
        print("作者：Alice_Ctoy")
        print("邮箱：ctoyych0@gmail.com")
        print("Github：https://github.com/com-in/WinToolsBox")
        print("© 2025 Copyright Alice_Ctoy. All rights reserved.")
        os.system("pause")
    elif choice == "S" or choice == "s":
        setting()
    elif choice == "B" or choice == "b":
        break
    else:
        print("没有找到此项功能，请重新输入！")
        os.system("pause")
    os.system("cls")
