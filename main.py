# 在此文件内写tkinter
import tkinter
from tkinter import messagebox

from spider import PersonInfo
from urlHandle import UrlInfo
from documentHandle import FileManager


def program() -> tuple:
    https_url = input_area.get("1.0", "end").split('\n')
    exist_url = entry0.get()
    target_url = entry1.get()
    person_data_list = []
    error_data_list = []
    for every_url in https_url:
        if not 'https' in every_url: 
            continue
        urlInfo = UrlInfo(url=every_url)
        url_state, tdi, bt = urlInfo.getInfo()
        if url_state == 'ok':
            siteInfo = PersonInfo(task_data_id=tdi, business_type=bt)
            siteState, tel_number, business_type = siteInfo.getInfo()
            if siteState == 'ok':
                person_data_list.append([(tel_number + '.0'), business_type, every_url])
            else:
                info = '获取网站信息时发生未知错误'
                error_data_list.append([every_url, info])
                continue
        else:
            # 记录错误url以及错误状态
            info = '解析域名时发生位置错误'
            error_data_list.append([every_url, info])
    
    if not person_data_list:
        return 'error', '没有需要写入的数据'
    
    fileManger = FileManager(exsit_url=exist_url, target_url=target_url, data_list=person_data_list)
    fileState, fileInfo = fileManger.writeXlsx()
    if fileState == 'ok':
        if not error_data_list:
            response = messagebox.showinfo('成功', '全部步骤完成！文件储存在' + fileInfo)
        else:
            content = '全部步骤完成，文件储存在' + fileInfo + '\n但有部分链接失败\n'
            for everyContent in error_data_list:
                content += everyContent[0] + ' 失败类型: ' + everyContent[1] + '\n'
            response = messagebox.showwarning('部分成功', content)
    else:
        response = messagebox.showerror('错误',('失败' + fileInfo))


if __name__ == '__main__':
    root = tkinter.Tk()
    
    root.title('自动控制工具')
    # 设置窗体大小
    root.geometry("800x600")
    text0 = tkinter.Label(root, text='在下方输入已有excel文件的路径(需要绝对路径，可不填)')
    text0.pack()

    entry0 = tkinter.Entry(root, width=60)
    entry0.pack()

    text1 = tkinter.Label(root, text='在下方输入excel文件导出的目标文件夹(需要绝对路径，可以不填): ')
    text1.pack()

    entry1 = tkinter.Entry(root, width=60)
    entry1.pack()

    text2 = tkinter.Label(root, text='在下方输入想要解析的网址: ')
    text2.pack()
    # 定义输入框
    input_area = tkinter.Text(root, width=95, height=30)
    input_area.pack()

    bt = tkinter.Button(root, height=2, command=program)
    bt['text'] = '下一步'
    bt.pack()

    root.mainloop()
