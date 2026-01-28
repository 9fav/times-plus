import tkinter as tk
from updater import check_update

# 定义软件版本号
APP_VERSION = "1.0.0"


# 1. 继承 tk.Frame，表示这个类是一个“增强版的托盘”
class CounterApp(tk.Frame):
    def __init__(self, master=None,):
        # 2. 调用父类的初始化，把地基打好
        super().__init__(master, background='lightgray')
        self.master = master
        self.pack(expand=True,)
        
        # 3. 定义一个【属性】来保存数据（这是类的记忆）
        self.count = 0 
        
        # 4. 调用创建零件的方法
        self.create_widgets()

    def create_widgets(self):
        # 5. 创建显示数字的标签，并挂载到 self 上
        self.label = tk.Label(self, text="当前数值: 0", font=("Arial", 16))
        self.label.pack(pady=10)

        # 6. 创建增加按钮，点击时调用 self.increase 方法
        self.add_button = tk.Button(self, text="点我加 1", command=self.increase)
        self.add_button.pack(side="left", padx=20)

        # 7. 创建重置按钮，点击时调用 self.reset 方法
        self.reset_button = tk.Button(self, text="重置", command=self.reset)
        self.reset_button.pack(side="left", padx=20)

        # 8. 创建减小按键
        self.minius_button = tk.Button(self, text='点我减 2', command=self.decrease)
        self.minius_button.pack(side="left", padx=20)

        # 9. 在界面底部显示版本号
        self.version_label = tk.Label(self, text=f"版本号: {APP_VERSION}", font=("Arial", 10), fg="gray")
        self.version_label.pack(side="bottom", pady=5)

    # --- 下面是【方法】，定义了对象的动作 ---
    def decrease(self):
        self.count = self.count - 2
        self.label.config(text=f"当前数值：{self.count}")

    def increase(self):
        self.count += 1
        self.label.config(text=f"当前数值: {self.count}")

    def reset(self):
        self.count = 0
        self.label.config(text="当前数值: 0")

# 启动程序
if __name__ == "__main__":
    # 启动前检查更新 check_update(APP_VERSION)
    root = tk.Tk()
    root.title(f"我的计数器 v{APP_VERSION}")  # 在标题栏显示版本号
    root.geometry("300x150")  # 设置窗口大小
    app = CounterApp(master=root)
    app.mainloop()
