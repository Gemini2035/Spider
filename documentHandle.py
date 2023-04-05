import os
import xlwings as Xw
import datetime

class FileManager:
    def __init__(self, url: str = '') -> None:
        self.__file_url = url
        self.__inner_data = []

    def getExistData(self) -> None:
        if self.__file_url == '': return
        wb = Xw.Book(self.__file_url)
        sht = wb.sheets[0]
        self.__inner_data = sht.range('A1').expand().value
        wb.close()

    def writeXlsx(self, data_list: list, target_url: str = './Output') -> str:
        self.getExistData()
        # 查重处理
        [self.__inner_data.append(data) for data in data_list if data not in self.__inner_data]
        try:
            app = Xw.App(visible=False, add_book=False)
            book = app.books.add()
            sht = book.sheets.add()
            for i in range(len(self.__inner_data)):
                position = 'A' + str(i + 1)
                sht.range(position).value = self.__inner_data[i]
            name = 'result' + datetime.date.today().__str__() + '-' + datetime.datetime.now().strftime('%H-%M-%S') + '.xlsx'
            book.save(os.path.join(target_url, name))
            book.close()
            app.quit()
            return '成功导出文件，文件位置: ' + target_url
        except:
            return '在写excel文件时发生未知错误'

