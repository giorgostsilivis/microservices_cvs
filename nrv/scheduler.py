import schedule
import main
import mail_parser
import time

def main_job():
    # os.system("python3.7 doc_handler.py")
    mail_parser.job_retrieve()
    main.do_it()

if __name__ == '__main__':
    schedule.every(20).seconds.do(main_job)

    while True:
        schedule.run_pending()
        time.sleep(3)
