import time
from datetime import datetime as dt

hosts_path = r'C:\Windows\System32\drivers\etc\hosts'
redirect = '127.0.0.1'
sites_to_kill = ['www.facebook.com', 'facebook.com', 'www.gmail.com']
seconds_of_work = 0

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 16) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        seconds = seconds_of_work % 60
        minutes = seconds_of_work // 60 % 60
        hours = seconds_of_work // 60 // 60 % 60
        print('Working Hours: {}:{}:{}'.format(hours, minutes, seconds))
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
    seconds_of_work += 1
    time.sleep(1000)
