import os,time,tkinter

def backup():
    global entry_source
    global entry_target
    source = entry_source.get()
    target_dir = entry_target.get()

    today_dir = target_dir + time.strftime('%Y%m%d')
    time_dir = time.strftime("%H%M%S")
    # 根据系统的不同，os.sep也不同，
    # 在Linux和Mac下, os.sep的值为'/'，
    # 而在Windows系统中，os.sep的值为'\'。
    touch = today_dir + os.sep + time_dir + '.zip'
    # -q ： 选项用来表示zip命令安静的工作
    # -r ： 选项用来标识zip命令对目录递归的工作，即包括对该文件和其子文件操作
    command_touch = "zip -qr " + touch +' '+ source

    print(command_touch)
    print(source)
    print(target_dir)
    if os.path.exists(today_dir)==0:
        os.mkdir(today_dir)
    if os.system(command_touch)==0:
        print("Success backup Up")
    else:
        print("Failed backup")

#从这里开始呢，则是开始界面的编写及布局
root = tkinter.Tk()
root.title('备份文件')
root.geometry("200x200")
#第一行的两个控件，Label:文本控件，Entry:输入框控件
lbl_source = tkinter.Label(root, text='源文件地址')
lbl_source.grid(row=0, column=0)
entry_source = tkinter.Entry(root)
entry_source.grid(row=0,column=1)
#第二行的两个控件
lbl_target = tkinter.Label(root, text='目标目录')
lbl_target.grid(row=1, column=0)
entry_target = tkinter.Entry(root)
entry_target.grid(row=1,column=1)
#第三行的一个按钮控件
button_back = tkinter.Button(root,text='备份')
button_back.grid(row=3, column=0)
button_back["command"] = backup
#界面的开始
root.mainloop()