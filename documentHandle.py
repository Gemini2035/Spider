import os
import xlwings as Xw
import datetime

class FileManager:
    def __init__(self, exsit_url: str = '', target_url: str = './Output', data_list: list = []) -> None:
        self.__file_url = exsit_url
        self.__inner_data = []
        self.__target_url = target_url
        self.__data_list = data_list

    def getExistData(self) -> None:
        if os.path.exists(self.__file_url):
            wb = Xw.Book(self.__file_url)
        else:
            wb = Xw.Book(r'./Input/test.xlsx')
        sht = wb.sheets[0]
        self.__inner_data = sht.range('A1').expand().value
        wb.close()

    def writeXlsx(self) -> tuple:
        try:
            self.getExistData()
        except:
            return 'error', '获取已存在excel表格时出现未知错误'
        # 查重处理
        [self.__inner_data.append(data) for data in self.__data_list if data not in self.__inner_data]

        try:
            app = Xw.App(visible=False, add_book=False)
            book = app.books.add()
            sht = book.sheets.add()
            for i in range(len(self.__inner_data)):
                position = 'A' + str(i + 1)
                sht.range(position).value = self.__inner_data[i]
            name = 'result' + datetime.date.today().__str__() + '-' + datetime.datetime.now().strftime('%H-%M-%S') + '.xlsx'
            if os.path.exists(self.__target_url):
                book.save(os.path.join(self.__target_url, name))
            else:
                book.save(os.path.join('./Output', name))
            book.close()
            app.quit()
            return 'ok', self.__target_url
        except:
            return 'error', '在写excel文件时发生未知错误'

