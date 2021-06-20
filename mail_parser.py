import imaplib
import base64
import os
import email
import datetime as dt
from getpass import getpass
import time
import logging
import pathlib
import imap_tools

def job_retrieve():
    try:
        # email_user = input('Email: ')
        email_user = 'demodeepsea@gmail.com'
        email_pass = ''
        # today = input('since eg 26-Jan-2021: ')
        today = '31-Jan-2021'

        port = 993

        mail = imaplib.IMAP4_SSL('imap.gmail.com',port)

        mail.login(email_user, email_pass)

        mail.select(mailbox='INBOX')

        # type, data = mail.search(None, 'ALL') #########
        type, data = mail.search(None,'UNSEEN', '(SINCE {0})'.format(today), 'HEADER FROM "gmail.com"')#dont forget to add an extra OR
        #type, data = mail.search(None,'UNSEEN', '(SINCE {0})'.format(today), 'OR OR HEADER FROM "seanergy.gr" HEADER FROM "deepsea.ai" HEADER FROM "gmail.com"')
        # print(result,datum)
        mail_ids = data[0]
        id_list = mail_ids.split()
        # print(id_list)
        for num in data[0].split():
            typ, data = mail.fetch(num, '(RFC822)' )
            raw_email = data[0][1]
        # converts byte literal to string removing b''
            raw_email_string = raw_email.decode('utf-8')
            email_message = email.message_from_string(raw_email_string)
        # downloading attachments
            for part in email_message.walk():
                if part.get_content_maintype() == 'multipart':
                    continue
                if part.get('Content-Disposition') is None:
                    continue
                fileName = part.get_filename()
                if fileName == None:
                    import random
                    fileName = str(random.random())
                stamp = '{0}_'.format(int(time.time()*1000000))
                if '.zip' not in fileName:
                    fileName = stamp+fileName
                if bool(fileName):
                    filePath = os.path.join('downloads/', fileName.replace(" ", "_"))
                    if not os.path.isfile(filePath) :
                        fp = open(filePath, 'wb')
                        fp.write(part.get_payload(decode=True))
                        fp.close()
                        subject = str(email_message).split("Subject: ", 1)[1].split("\nTo:", 1)[0]
                        now = dt.datetime.now()
                        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
                        logger.info(f'{current_time}:  service: mail_parser, Downloaded "{fileName}" from email titled "{subject}"')
        mail.close()
        mail.logout()


    except:
        now = dt.datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        # logger.critical(f'{current_time}: mail_parser failed', exc_info=True)
        pass
