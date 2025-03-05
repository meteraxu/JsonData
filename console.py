from core import JsonData
import config
from core import system_method

class console_action:
    def choice_first(self):
        print("First Doing")

class console_manner:
    def __init__(self):
        self.system_method = system_method()
        self.console_carry = console_action()
        self.console_per = {"1": lambda: self.console_carry.choice_first()}
        print("欢迎使用JsonData(Delta-developed) Console!")
        init_db = input("请输入要加载的数据库文件:")
        self.db = JsonData(str(init_db))
        self.console_main()
    def console_main(self):
        print("___控制面板___")
        print("1.执行JDB语句\n"
              "2.加密功能(Beta)\n"
              "e.退出面板")
        print("_____________")
        input_code = input("选项:")
        if str(input_code) in self.console_per:
            self.console_per[str(input_code)]()
        else:
            self.system_method.clean_screen()
            print("请输入正确的选项")
            self.console_main()