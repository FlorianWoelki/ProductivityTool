import time
import thread
from datetime import datetime as dt
from sys import platform

hosts_path = r'C:\Windows\System32\drivers\etc\hosts'
if platform == 'darwin' or platform == 'linux' or platform == 'linux2':
    hosts_path = r'/etc/hosts'

redirect = '127.0.0.1'
sites_to_kill = ['www.facebook.com', 'facebook.com', 'www.gmail.com']


def run_tool():
    seconds_of_work = 0

    while True:
        if dt(dt.now().year, dt.now().month, dt.now().day, 16) < dt.now() < dt(dt.now().year, dt.now().month,
                                                                               dt.now().day, 17):
            seconds = seconds_of_work % 60
            minutes = seconds_of_work // 60 % 60
            hours = seconds_of_work // 60 // 60 % 60
            print('Working Hours: {}:{}:{}'.format('0' + hours if hours < 10 else hours,
                                                   '0' + minutes if minutes < 10 else minutes,
                                                   '0' + seconds if seconds < 10 else seconds))
            seconds_of_work += 1
            with open(hosts_path, 'r+') as file:
                content = file.read()
                for site in sites_to_kill:
                    if site in content:
                        pass
                    else:
                        file.write(redirect + ' ' + site + '\n')
        else:
            with open(hosts_path, 'r+') as file:
                content = file.readlines()
                file.seek(0)
                for line in content:
                    if not any(site in line for site in sites_to_kill):
                        file.write(line)
                file.truncate()
            print('Time to get some rest!')
        time.sleep(1000)


try:
    thread.start_new_thread(run_tool())
except:
    print 'Error: Unable to start thread'
