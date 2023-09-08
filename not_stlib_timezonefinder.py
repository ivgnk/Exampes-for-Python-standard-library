'''
https://pypi.org/project/timezonefinder/
'''
import datetime

import inspect
import geopy # geopy is a Python client for several popular geocoding web services  https://geopy.readthedocs.io/en/stable/

import stun  # https://pypi.org/project/pystun3-fix/
import pymyip # https://ru.stackoverflow.com/questions/133137/Нужно-узнать-ip-адрес-своего-компьютера-в-интернете-в-python

import time
import timezonefinder
import pprint
from timezonefinder import TimezoneFinder
import http.client

pack_name = 'timezonefinder'

def paktc():
    print('Нажмите любую клавишу')
    input()

def dir_of_pack(pack_name:str):
    print('\n === spec dir of ',pack_name)
    lst = dir(pack_name);  print(type(lst))
    pprint.pprint(lst, width=40)


def view_packet_object(pack_name:str)->None:
    # for i in dir(pack_name):
    #     print(i, "  ", type(getattr(pack_name, i)))
    print(timezonefinder)
    # https://docs.python.org/3/library/functions.html#dir

    # print('\n === dir of ',pack_name)
    # lst = dir(timezonefinder);  print(type(lst))
    # pprint.pprint(lst, width=40)
    #
    # print('\n === vars')
    # lst = vars(timezonefinder); print(type(lst))
    # pprint.pprint(lst, width=40)

def get_my_ip():
    # Нужно узнать ip адрес своего компьютера в интернете в Python
    # https://ru.stackoverflow.com/questions/133137/Нужно-узнать-ip-адрес-своего-компьютера-в-интернете-в-python

    print('\nВыполняемая функция = ',inspect.currentframe().f_code.co_name)
    conn = http.client.HTTPConnection("ifconfig.me")
    conn.request("GET", "/ip")
    res = conn.getresponse().read()
    print(type(res))
    print(res)

    # Что делает символ «b» перед строковым литералом?
    # https://stackoverflow.com/questions/6269765/what-does-the-b-character-do-in-front-of-a-string-literal
    s = str(res.decode('UTF-8'))
    print(type(s))
    print(s)

    #------- Второй вариант получения ip
    # !!!!! https://pypi.org/project/pystun3-fix/ см. использование
    print('\nВторой вариант получения ip')
    print('-- Первый вариант вывода')
    s = stun.get_ip_info()
    print(f'{type(s)=}')
    print(f'{s=}')
    print('  map(lambda x: print(x), s)  ')
    for i in s: print(f'{i=}')

    print('\n-- Второй вариант вывода')
    nat_type, external_ip, external_port = stun.get_ip_info()
    print(f'{nat_type=}      {type(nat_type)=}')
    print(f'{external_ip=}   {type(external_ip)=}')
    print(f'{external_port=} {type(external_port)=}')
    print()

    #------- Третий вариант получения ip
    # https://stackoverflow.com/questions/24678308/how-to-find-location-with-ip-address-in-python



def work_with_timezone():
    # https://stackoverflow.com/questions/1111056/get-time-zone-information-of-the-system-in-python
    print('\nВыполняемая функция = ',inspect.currentframe().f_code.co_name)
    print('\n === time')
    print(time)
    print(f'{time.timezone=}')
    print(f'Моя временная зона {time.tzname=}')
    # paktc()
    # lst = dir(time)
    # pprint.pprint(lst, width=40)

    # https://stackoverflow.com/questions/1111056/get-time-zone-information-of-the-system-in-python
    offset = time.timezone if (time.localtime().tm_isdst == 0) else time.altzone
    res =  offset / 60 / 60 * -1
    print('offset =' ,res)
    # https://ru.wikipedia.org/wiki/Время_в_России
    # offset =5  (UTC+5)

    print('\n-- Второй вариант определения timezone')
    # https://stackoverflow.com/questions/1111056/get-time-zone-information-of-the-system-in-python
    # https://stackoverflow.com/questions/2720319/python-figure-out-local-timezone/39079819#39079819
    tz_string = datetime.datetime.now().astimezone().tzname()
    print(f'{tz_string=}')
    tz_string = datetime.datetime.now().astimezone().tzinfo
    print(f'{tz_string=}')

    local_timezone = datetime.datetime.utcnow().astimezone().tzinfo
    print(f'{local_timezone=}')

def work_with_timezonefinder():
    print('\nВыполняемая функция = ',inspect.currentframe().f_code.co_name)
    tf = TimezoneFinder()  # reuse

    query_points = [(13.358, 52.5061)]
    for lng, lat in query_points:
        print()
        tz = tf.timezone_at(lng=lng, lat=lat)  # 'Europe/Berlin'
        print(type(tz))
        print(f'Временная зона {tz=}')

if __name__ == "__main__":
    # get_my_ip()

    # view_packet_object(pack_name)
    work_with_timezone()
    work_with_timezonefinder()
