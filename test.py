# import time

# def timestamp_datetime(value):
#      format = 
#      dt  = time.strftime('%Y-%m-%d %H:%M:%S' , time.localtime(value))
#      return dt

# print(timestamp_datetime(int(1684202477808 / 1000)))

# def datetime_timestamp(dt):
#       #dt为字符串
#       #中间过程，一般都需要将字符串转化为时间数组
#       time.strptime(dt,  '%Y-%m-%d %H:%M:%S' )
#       ## time.struct_time(tm_year=2012, tm_mon=3, tm_mday=28, tm_hour=6, tm_min=53, tm_sec=40, tm_wday=2, tm_yday=88, tm_isdst=-1)
#       #将"2012-03-28 06:53:40"转化为时间戳
#       s  = time.mktime(time.strptime(dt,  '%Y-%m-%d %H:%M:%S' ))
#       return int (s)

# print(datetime_timestamp('2023-05-16 10:01:17'))