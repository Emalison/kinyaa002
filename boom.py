import schedule
import time
from like import job


#schedule.every(10).seconds.do(job)
schedule.every(30).minutes.do(job)
#schedule.every().hour.do(job)
#schedule.every().day.at("09:55").do(job_function)
#schedule.every().day.at("06:20").do(job_function)
#schedule.every().day.at("07:32").do(job_function)
#schedule.every().day.at("08:36").do(job_function)
#schedule.every().day.at("09:39").do(job_function)
#schedule.every().day.at("10:42").do(job_function)
#schedule.every().day.at("11:47").do(job_function)
#schedule.every().day.at("12:45").do(job_function)
#schedule.every().day.at("13:50").do(job_function)
#schedule.every().day.at("14:45").do(job_function)
#schedule.every(5).to(10).minutes.do(job)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job_function)


while True:
    schedule.run_pending()
    time.sleep(1)
