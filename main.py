# 在此文件内写pygame

from spider import PersonInfo
from urlHandle import UrlInfo

if __name__ == '__main__':
    testInfo = UrlInfo(url='https://www.xfyeta.com/mobile/#/detail/11075/603638740077910138')
    testInfo.setInfo()
    task_data_id, business_type = testInfo.getInfo()
    test_spider = PersonInfo(task_data_id=task_data_id, business_type=business_type)
    test_spider.setInfo()
    print(test_spider.getInfo())

