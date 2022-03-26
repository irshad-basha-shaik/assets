from crontab import CronTab

my_cron = CronTab(user='roy')
job = my_cron.new(command='python /home/roy/writeDate.py')
job.minute.every(1)

my_cron.write()
"""
from crontab import CronTab
cron = CronTab(user='root')
job = cron.new(command='echo hello_world')
job.minute.every(1)
cron.write()
with CronTab(user='root') as cron:
    job = cron.new(command='echo hello_world')
    job.minute.every(1)
print('cron.write() was just executed')
"""