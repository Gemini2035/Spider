
class UrlInfo: 
    def __init__(self, url: str) -> None:
        self.__url = url
        self.__task_data_id = ''
        self.__business_type = ''

    def setInfo(self) -> None:
        strArray = self.__url.split('/')
        self.__task_data_id = strArray[len(strArray) - 1]
        self.__business_type = strArray[len(strArray) - 2]

    def getInfo(self) -> tuple:
        self.setInfo()
        return self.__task_data_id, self.__business_type

