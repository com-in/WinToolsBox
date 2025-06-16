import os
from mcstatus import JavaServer

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
current_language = "zh"  # 默认中文

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

# 定义主界面 - 中文
def main_page():
    print("========Windows Tools Box Version 1.1.0=============")
    print("        [1]磁盘修复            [2]文件删除             ")
    print("        [3]格式化              [4]网络连通性测试        ")
    print("        [5]任务管理器          [6]Minecraft服务器查询   ")
    print("        [7]系统信息                                    ") 
    print("        [A]关于")
    print("        [S]设置               ")
    print("        [B]退出               ")
    print("====================================================")

# 主界面 - 英文
def main_page_en():
    print("========Windows Tools Box Version 1.1.0=============")
    print("        [1]Disk Repair        [2]File Delete          ")
    print("        [3]Format Disk        [4]Network Test         ")
    print("        [5]Task Manager       [6]Minecraft Server Query")
    print("        [7]System Information                         ") 
    print("        [A]About")
    print("        [S]Settings           ")
    print("        [B]Exit               ")
    print("====================================================")

# 主界面 - 俄语
def main_page_ru():
    print("========Windows Tools Box Version 1.1.0=============")
    print("        [1]Ремонт диска      [2]Удаление файлов       ")
    print("        [3]Форматирование     [4]Проверка сети         ")
    print("        [5]Диспетчер задач    [6]Запрос сервера Minecraft")
    print("        [7]Информация о системе                      ") 
    print("        [A]О программе")
    print("        [S]Настройки         ")
    print("        [B]Выход            ")
    print("====================================================")

# 主界面 - 西班牙语
def main_page_es():
    print("========Windows Tools Box Version 1.1.0=============")
    print("        [1]Reparar disco      [2]Eliminar archivos     ")
    print("        [3]Formatear          [4]Prueba de red         ")
    print("        [5]Administrador de tareas [6]Consulta servidor Minecraft")
    print("        [7]Información del sistema                    ") 
    print("        [A]Acerca de")
    print("        [S]Configuración      ")
    print("        [B]Salir             ")
    print("====================================================")

# 格式化motd - 中文
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

# 查询MC服务器 - 中文
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
              """)
    except Exception as e:
        print(f"查询失败，错误信息：{e}")
    os.system("pause")

# 查询MC服务器 - 英文
def query_minecraft_server_en():
    os.system("cls")
    server_address = input("Enter Minecraft server address (format: IP:port, default port is 25565): ")
    if ':' not in server_address:
        server_address = f"{server_address}:25565"
    try:
        server = JavaServer.lookup(server_address)
        status = server.status()
        print(f"Server status: Online")
        print(f"Players online: {status.players.online}")
        version_name = status.version.name.lower()
        
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
        
        server_type = "Other"
        for key in server_type_mapping:
            if key in version_name:
                server_type = server_type_mapping[key]
                break
        
        print(f"Server type: {server_type}")
        print(f"""Motd:
              {format_motd(str(status.description))}
              """)
    except Exception as e:
        print(f"Query failed, error: {e}")
    os.system("pause")

# 查询MC服务器 - 俄语
def query_minecraft_server_ru():
    os.system("cls")
    server_address = input("Введите адрес сервера Minecraft (формат: IP:порт, по умолчанию порт 25565): ")
    if ':' not in server_address:
        server_address = f"{server_address}:25565"
    try:
        server = JavaServer.lookup(server_address)
        status = server.status()
        print(f"Статус сервера: Онлайн")
        print(f"Игроков онлайн: {status.players.online}")
        version_name = status.version.name.lower()
        
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
        
        server_type = "Другой"
        for key in server_type_mapping:
            if key in version_name:
                server_type = server_type_mapping[key]
                break
        
        print(f"Тип сервера: {server_type}")
        print(f"""Motd:
              {format_motd(str(status.description))}
              """)
    except Exception as e:
        print(f"Ошибка запроса: {e}")
    os.system("pause")

# 查询MC服务器 - 西班牙语
def query_minecraft_server_es():
    os.system("cls")
    server_address = input("Ingrese la dirección del servidor Minecraft (formato: IP:puerto, puerto predeterminado es 25565): ")
    if ':' not in server_address:
        server_address = f"{server_address}:25565"
    try:
        server = JavaServer.lookup(server_address)
        status = server.status()
        print(f"Estado del servidor: En línea")
        print(f"Jugadores en línea: {status.players.online}")
        version_name = status.version.name.lower()
        
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
        
        server_type = "Otro"
        for key in server_type_mapping:
            if key in version_name:
                server_type = server_type_mapping[key]
                break
        
        print(f"Tipo de servidor: {server_type}")
        print(f"""Motd:
              {format_motd(str(status.description))}
              """)
    except Exception as e:
        print(f"Error en la consulta: {e}")
    os.system("pause")

# 磁盘修复 - 中文
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

# 磁盘修复 - 英文
def fix_disk_function_en():
    global fix_disk
    fix_disk = input("Enter drive letter: ")
    if len(fix_disk) == 2:
        print("Starting repair...")
        os.system(f"chkdsk {fix_disk} /F")
        print("Repair completed!")
        os.system("pause")
    elif len(fix_disk) == 1:
        print("Starting repair...")
        os.system(f"chkdsk {fix_disk}: /F")
        print("Repair completed!")
        os.system("pause")
    else:
        print("Oops...invalid drive letter")
        os.system("pause")

# 磁盘修复 - 俄语
def fix_disk_function_ru():
    global fix_disk
    fix_disk = input("Введите букву диска: ")
    if len(fix_disk) == 2:
        print("Начинаем ремонт...")
        os.system(f"chkdsk {fix_disk} /F")
        print("Ремонт завершен!")
        os.system("pause")
    elif len(fix_disk) == 1:
        print("Начинаем ремонт...")
        os.system(f"chkdsk {fix_disk}: /F")
        print("Ремонт завершен!")
        os.system("pause")
    else:
        print("Ой...неправильная буква диска")
        os.system("pause")

# 磁盘修复 - 西班牙语
def fix_disk_function_es():
    global fix_disk
    fix_disk = input("Ingrese la letra de la unidad: ")
    if len(fix_disk) == 2:
        print("Iniciando reparación...")
        os.system(f"chkdsk {fix_disk} /F")
        print("¡Reparación completada!")
        os.system("pause")
    elif len(fix_disk) == 1:
        print("Iniciando reparación...")
        os.system(f"chkdsk {fix_disk}: /F")
        print("¡Reparación completada!")
        os.system("pause")
    else:
        print("Oops...letra de unidad no válida")
        os.system("pause")

# 文件删除 - 中文
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

# 文件删除 - 英文
def file_del_en():
    global delete_file
    delete_file = input("Enter file or folder path: ")
    if os.path.exists(delete_file):
        print("Deleting...")
        os.system(f"del /f /s /q {delete_file}")
        print("Deletion completed!")
        os.system("pause")
    else:
        print("Oops...path does not exist")
        os.system("pause")

# 文件删除 - 俄语
def file_del_ru():
    global delete_file
    delete_file = input("Введите путь к файлу или папке: ")
    if os.path.exists(delete_file):
        print("Удаление...")
        os.system(f"del /f /s /q {delete_file}")
        print("Удаление завершено!")
        os.system("pause")
    else:
        print("Ой...путь не существует")
        os.system("pause")

# 文件删除 - 西班牙语
def file_del_es():
    global delete_file
    delete_file = input("Ingrese la ruta del archivo o carpeta: ")
    if os.path.exists(delete_file):
        print("Eliminando...")
        os.system(f"del /f /s /q {delete_file}")
        print("¡Eliminación completada!")
        os.system("pause")
    else:
        print("Oops...la ruta no existe")
        os.system("pause")

# 格式化 - 中文
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

# 格式化 - 英文
def format_disk_function_en():
    global format_disk
    format_disk = input("Enter drive letter: ")
    if len(format_disk) == 2:
        print("Formatting...")
        os.system(f"format {format_disk}")
        print("Format completed!")
        os.system("pause")
    elif len(format_disk) == 1:
        print("Formatting...")
        os.system(f"format {format_disk}:")
        print("Format completed!")
        os.system("pause")
    else:
        print("Oops...invalid drive letter")
        os.system("pause")
    os.system("pause")

# 格式化 - 俄语
def format_disk_function_ru():
    global format_disk
    format_disk = input("Введите букву диска: ")
    if len(format_disk) == 2:
        print("Форматирование...")
        os.system(f"format {format_disk}")
        print("Форматирование завершено!")
        os.system("pause")
    elif len(format_disk) == 1:
        print("Форматирование...")
        os.system(f"format {format_disk}:")
        print("Форматирование завершено!")
        os.system("pause")
    else:
        print("Ой...неправильная буква диска")
        os.system("pause")
    os.system("pause")

# 格式化 - 西班牙语
def format_disk_function_es():
    global format_disk
    format_disk = input("Ingrese la letra de la unidad: ")
    if len(format_disk) == 2:
        print("Formateando...")
        os.system(f"format {format_disk}")
        print("¡Formateo completado!")
        os.system("pause")
    elif len(format_disk) == 1:
        print("Formateando...")
        os.system(f"format {format_disk}:")
        print("¡Formateo completado!")
        os.system("pause")
    else:
        print("Oops...letra de unidad no válida")
        os.system("pause")
    os.system("pause")

# 网络测试 - 中文
def network_test():
    global address  
    address = input("请输入地址：")
    os.system(f"ping {address}")
    os.system("pause")

# 网络测试 - 英文
def network_test_en():
    global address  
    address = input("Enter address: ")
    os.system(f"ping {address}")
    os.system("pause")

# 网络测试 - 俄语
def network_test_ru():
    global address  
    address = input("Введите адрес: ")
    os.system(f"ping {address}")
    os.system("pause")

# 网络测试 - 西班牙语
def network_test_es():
    global address  
    address = input("Ingrese la dirección: ")
    os.system(f"ping {address}")
    os.system("pause")

# 任务管理器 - 中文
def task_manager():
    os.system("taskmgr")

# 任务管理器 - 英文
def task_manager_en():
    os.system("taskmgr")

# 任务管理器 - 俄语
def task_manager_ru():
    os.system("taskmgr")

# 任务管理器 - 西班牙语
def task_manager_es():
    os.system("taskmgr")

# 设置 - 中文
def setting():
    global set_choice
    os.system("cls")
    print("=======设置=======")
    print("   [1]字符颜色")
    print("   [2]语言选择")
    print("")
    print("   [B]返回主菜单")
    print("=================")
    set_choice = input("请输入选项：")
    if set_choice == "1":
        set_color()
    elif set_choice == "2":
        change_language()
    elif set_choice == "B" or set_choice == "b":
        if current_language == "zh":
            main_page()
        elif current_language == "en":
            main_page_en()
        elif current_language == "ru":
            main_page_ru()
        elif current_language == "es":
            main_page_es()
    else:
        print("啊哦...不是正确的选项哦")
        os.system("pause")
        os.system("cls")
        setting()

# 设置 - 英文
def setting_en():
    global set_choice
    os.system("cls")
    print("=======Settings=======")
    print("   [1]Text Color")
    print("   [2]Language")
    print("")
    print("   [B]Back to Main Menu")
    print("======================")
    set_choice = input("Enter option: ")
    if set_choice == "1":
        set_color_en()
    elif set_choice == "2":
        change_language()
    elif set_choice == "B" or set_choice == "b":
        if current_language == "zh":
            main_page()
        elif current_language == "en":
            main_page_en()
        elif current_language == "ru":
            main_page_ru()
        elif current_language == "es":
            main_page_es()
    else:
        print("Oops...invalid option")
        os.system("pause")
        os.system("cls")
        setting_en()

# 设置 - 俄语
def setting_ru():
    global set_choice
    os.system("cls")
    print("=======Настройки=======")
    print("   [1]Цвет текста")
    print("   [2]Язык")
    print("")
    print("   [B]Назад в главное меню")
    print("======================")
    set_choice = input("Введите вариант: ")
    if set_choice == "1":
        set_color_ru()
    elif set_choice == "2":
        change_language()
    elif set_choice == "B" or set_choice == "b":
        if current_language == "zh":
            main_page()
        elif current_language == "en":
            main_page_en()
        elif current_language == "ru":
            main_page_ru()
        elif current_language == "es":
            main_page_es()
    else:
        print("Ой...неправильный вариант")
        os.system("pause")
        os.system("cls")
        setting_ru()

# 设置 - 西班牙语
def setting_es():
    global set_choice
    os.system("cls")
    print("=======Configuración=======")
    print("   [1]Color del texto")
    print("   [2]Idioma")
    print("")
    print("   [B]Volver al menú principal")
    print("===========================")
    set_choice = input("Ingrese la opción: ")
    if set_choice == "1":
        set_color_es()
    elif set_choice == "2":
        change_language()
    elif set_choice == "B" or set_choice == "b":
        if current_language == "zh":
            main_page()
        elif current_language == "en":
            main_page_en()
        elif current_language == "ru":
            main_page_ru()
        elif current_language == "es":
            main_page_es()
    else:
        print("Oops...opción no válida")
        os.system("pause")
        os.system("cls")
        setting_es()

# 设置颜色 - 中文
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

# 设置颜色 - 英文
def set_color_en():
    global word_color_choice
    os.system("cls")
    print("""=========Color Codes=========
        0 = Black      8 = Gray
        1 = Blue       9 = Light Blue
        2 = Green      A = Light Green
        3 = Aqua       B = Light Aqua
        4 = Red        C = Light Red
        5 = Purple     D = Light Purple
        6 = Yellow     E = Light Yellow
        7 = White      F = Bright White
        """)
    word_color_choice = input("Enter color: ")
    os.system(f"color {word_color_choice}")
    os.system("cls")
    setting_en()

# 设置颜色 - 俄语
def set_color_ru():
    global word_color_choice
    os.system("cls")
    print("""=========Цвета=========
        0 = Черный     8 = Серый
        1 = Синий      9 = Светло-синий
        2 = Зеленый    A = Светло-зеленый
        3 = Бирюзовый  B = Светло-бирюзовый
        4 = Красный    C = Светло-красный
        5 = Фиолетовый D = Светло-фиолетовый
        6 = Желтый     E = Светло-желтый
        7 = Белый      F = Ярко-белый
        """)
    word_color_choice = input("Введите цвет: ")
    os.system(f"color {word_color_choice}")
    os.system("cls")
    setting_ru()

# 设置颜色 - 西班牙语
def set_color_es():
    global word_color_choice
    os.system("cls")
    print("""=========Códigos de color=========
        0 = Negro      8 = Gris
        1 = Azul       9 = Azul claro
        2 = Verde      A = Verde claro
        3 = Aguamarina B = Aguamarina claro
        4 = Rojo       C = Rojo claro
        5 = Morado     D = Morado claro
        6 = Amarillo   E = Amarillo claro
        7 = Blanco     F = Blanco brillante
        """)
    word_color_choice = input("Ingrese el color: ")
    os.system(f"color {word_color_choice}")
    os.system("cls")
    setting_es()

# 系统信息 - 中文
def system_info():
    os.system("cls")
    os.system("systeminfo")
    os.system("pause")

# 系统信息 - 英文
def system_info_en():
    os.system("cls")
    os.system("systeminfo")
    os.system("pause")

# 系统信息 - 俄语
def system_info_ru():
    os.system("cls")
    os.system("systeminfo")
    os.system("pause")

# 系统信息 - 西班牙语
def system_info_es():
    os.system("cls")
    os.system("systeminfo")
    os.system("pause")

# 语言切换函数
def change_language():
    global current_language
    os.system("cls")
    print("=======语言选择=======")
    print("   [1]中文")
    print("   [2]English")
    print("   [3]Русский")
    print("   [4]Español")
    print("")
    print("   [B]返回")
    print("====================")
    lang_choice = input("请选择语言: ")
    if lang_choice == "1":
        current_language = "zh"
    elif lang_choice == "2":
        current_language = "en"
    elif lang_choice == "3":
        current_language = "ru"
    elif lang_choice == "4":
        current_language = "es"
    elif lang_choice == "B" or lang_choice == "b":
        setting()
    else:
        print("无效选择")
        os.system("pause")
    setting()

# 主循环
while True:
    os.system("cls")
    if current_language == "zh":
        main_page()
        choice = input("请输入选项：")
    elif current_language == "en":
        main_page_en()
        choice = input("Enter option: ")
    elif current_language == "ru":
        main_page_ru()
        choice = input("Введите вариант: ")
    elif current_language == "es":
        main_page_es()
        choice = input("Ingrese la opción: ")
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
        if current_language == "zh":
            print("Windows Tools Box")
            print("作者：Alice_Ctoy")
            print("邮箱：ctoyych0@gmail.com")
            print("Github：https://github.com/com-in/WinToolsBox")
            print("© 2025 Copyright Alice_Ctoy. All rights reserved.")
        elif current_language == "en":
            print("Windows Tools Box")
            print("Author: Alice_Ctoy")
            print("Email: ctoyych0@gmail.com")
            print("Github: https://github.com/com-in/WinToolsBox")
            print("© 2025 Copyright Alice_Ctoy. All rights reserved.")
        elif current_language == "ru":
            print("Windows Tools Box")
            print("Автор: Alice_Ctoy")
            print("Эл. почта: ctoyych0@gmail.com")
            print("Github: https://github.com/com-in/WinToolsBox")
            print("© 2025 Copyright Alice_Ctoy. All rights reserved.")
        elif current_language == "es":
            print("Windows Tools Box")
            print("Autor: Alice_Ctoy")
            print("Correo: ctoyych0@gmail.com")
            print("Github: https://github.com/com-in/WinToolsBox")
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
