import requests, json

class PersonInfo:
    def __init__(self, task_data_id: str, business_type: str) -> None:
        self.__url = 'https://www.xfyeta.com/taichi-data-api/api/v2/outbound/11075/queryTaskDataReport?token='
        self.__data = {
            "taskDataId": task_data_id,
            "business_id": business_type,
            "channelCode": 2,
            "pageIndex": 1,
            "pageSize": 1,
            "order": "time_callout desc"
        }
        self.__headers = {
            "cookie": "Hm_lvt_4fe9fdb47293c312e90e4396a4c7ac38=1680599377; Hm_lpvt_4fe9fdb47293c312e90e4396a4c7ac38=1680607958",
            "referer": "https://www.xfyeta.com/mobile/",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
        }
        
        self.__business_type = ""
        self.__tel_number = ""
    
    def setInfo(self) -> None:
        response = requests.post(self.__url, data=json.dumps(self.__data), headers=self.__headers).text
        self.__business_type = response[response.find('task_name') ::].split(':"')[1].split('"')[0]
        self.__tel_number = response[response.find('tel_number') ::].split(':"')[1].split('"')[0]

    def getInfo(self) -> tuple:
        state = ''
        try:
            self.setInfo()
            state = 'ok'
        except:
            state = 'error'
        return state, self.__tel_number, self.__business_type