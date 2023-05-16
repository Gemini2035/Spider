import requests, json, time

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
        self.__ai_log = ""
        self.__person_log = ""
        self.__time = ""
        self.__tag_intention = ""
    
    def setInfo(self) -> None:
        response = json.loads(requests.post(self.__url, data=json.dumps(self.__data), headers=self.__headers).text)['result']['rows']
        # print(response)
        self.__business_type = response[0]['task_name']
        self.__tel_number = response[0]['tel_number']
        handle_data = json.loads(response[0]['dialog'])
        for every_data in handle_data:
            self.__ai_log += (every_data['output'] + '\n')
            self.__person_log += (every_data['input'] + '\n')
        time_string = response[0]['time_callout']
        self.__time = time.strftime('%Y-%m-%d %H:%M:%S' , time.localtime(int(time_string[: len(time_string) - 3])))
        self.__tag_intention = response[0]['tag_intention']

    def getInfo(self) -> tuple:
        state = ''
        try:
            self.setInfo()
            state = 'ok'
        except:
            state = 'error'
        return state, self.__tel_number, self.__business_type, self.__ai_log, self.__person_log, self.__time, self.__tag_intention