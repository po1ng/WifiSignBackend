from app.constants import constants
import datetime
import time


def response_dict(status, message='', data=None):
    if not message:
        message = constants[status]
    if data is None:
        data = {}
    return {'status': status, 'message': message, 'data': data}


def get_now_datetime():
    now_hour = time.strftime('%H')
    now_min = time.strftime('%M')
    now_sec = time.strftime('%S')
    now_time = datetime.time(int(now_hour), int(now_min), int(now_sec))
    return now_time


def get_now_time():
    now_time = time.strftime('%H:%M:%S')
    return now_time


def get_class_num():
    now_time = get_now_datetime()
    info = {}
    class_time_start_1 = datetime.time(8, 0, 0)
    class_time_end_1 = datetime.time(10, 0, 0)
    class_time_start_2 = datetime.time(10, 5, 0)
    class_time_end_2 = datetime.time(12, 0, 0)
    class_time_start_3 = datetime.time(14, 30, 0)
    class_time_end_3 = datetime.time(16, 0, 0)
    class_time_start_4 = datetime.time(16, 0, 0)
    class_time_end_4 = datetime.time(18, 0, 0)
    if now_time > class_time_start_1 and now_time < class_time_end_1:
        info['start_time'] = '8'
        info['class_num'] = '1'
    elif now_time > class_time_start_2 and now_time < class_time_end_2:
        info['start_time'] = '10'
        info['class_num'] = '2'
    elif now_time > class_time_start_3 and now_time < class_time_end_3:
        info['start_time'] = '14'
        info['class_num'] = '3'
    elif now_time > class_time_start_4 and now_time < class_time_end_4:
        info['start_time'] = '16'
        info['class_num'] = '4'
    else:
        info['start_time'] = time.strftime('%H')
        info['class_num'] = '5'
    return info


def get_date():
    today_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    return today_date