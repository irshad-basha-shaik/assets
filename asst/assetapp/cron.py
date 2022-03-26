import os

def my_cron_job(self, *messages, **kwargs):
    ip_list = ['127.0.0.1', '192.168.1.180','10.162.10.254', '103.140.18.78', '192.168.1.102', '127.0.0.1', '192.168.1.180']
    for ip in ip_list:
        response = os.popen(f"ping {ip}").read()
        if "Received = 4" in response:
            print(f"UP {ip} Ping Successful")
            status = True
        else:
            print(f"DOWN {ip} Ping Unsuccessful")
            status = False
        return status
"""def make_log(self, *messages, **kwargs):
    ip_list = ['10.162.10.254','103.140.18.78','192.168.1.102','127.0.0.1','192.168.1.180']
    for ip in ip_list:
        response = os.popen(f"ping {ip}").read()
        if "Received = 4" in response:
            print(f"UP {ip} Ping Successful")
        else:
            print(f"DOWN {ip} Ping Unsuccessful")
    cron_log = self.cron_log

    cron_job      = getattr(self, 'cron_job', self.cron_job_class)
    cron_log.code = cron_job.code"""
