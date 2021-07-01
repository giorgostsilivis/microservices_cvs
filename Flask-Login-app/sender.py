from flask import Flask
from flask_mail import Mail, Message
import pandas as pd
import redis_test
import os
import sqlite3
from pretty_html_table import build_table
import sqlalchemy

app = Flask(__name__)
mail= Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'demodeepsea@gmail.com'
app.config['MAIL_PASSWORD'] = 'wuhhwafxtuoyhkpa'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def index():
    USER = ''
    cnx = sqlite3.connect('/home/giorgos/Desktop/microservices_cvs/db.sqlite')
    a = "SELECT * FROM class_table"
    df = pd.read_sql_query(a, cnx)
    html_table_blue_light = build_table(df[df['Class']=='A CLASS'], 'green_light')
    start = f"""<body style="background-color:powderblue;">
                        <table width="100%" height="100%" style="background-color:#FFFFE0;">
                        <tr>
                            <td width="100%" height="100%" bgcolor="#a6a6a6">
                            <p style="font-family:century gothic; font-size:20px; color:#0E1D2D; text-align:center;font-weight:bold">EMPLOYEE <span style="color:#FFFFE0;font-weight:bold">RANKING</span></p>
                            <strong style="font-family:century gothic; font-size:15px; color:#0E1D2D;text-align:left">{'Green table contains recommended employees'}</strong></br>
                            <strong style="font-family:century gothic; font-size:20px; color:#0E1D2D;text-align:left"><i style="color:#0E1D2D;"></i> {USER}</strong>
                            """
    end =                 """
                            <p><i style="font-family:century gothic; color:#0E1D2D;">end of page</i></p>
                            </td>
                        </tr>
                    </table>"""
    cnx.close()
    # df= pd.read_csv('mail.csv')
    # email = df['0'][0]
    email = redis_test.redis_out()
    msg = Message('cv classifier', sender = 'demodeepsea@gmail.com', recipients = [email])
    msg.body = "This is a positive feedback mail"
    msg.html = start+html_table_blue_light+end
    mail.send(msg)
    return "Sent"

if __name__ == '__main__':
   app.run(host='localhost',port='3000',debug = True)









# import pandas as pd
# import yagmail
# import sqlite3
# import sqlalchemy
# from flask import Flask,request
# from myproject.forms import ContactForm
# import requests

# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def home():
#     form = ContactForm()
#     email=form.email.data

#     # def send_mails(email):
#     try:
#         cnx = sqlite3.connect('db.sqlite')
#         df = pd.read_sql_query("SELECT * FROM class_table", cnx)
#         output = build_table(df, 'grey_light',font_size = 'medium', font_family = 'Century Gothic',text_align = 'left')
#         yag = yagmail.SMTP('demodeepsea@gmail.com', '2WSX@wsx3EDC#edc')
#         yag.send(email, 'CV Classifier', contents=output)
#     except:
#         output = build_table(df, 'grey_light',font_size = 'medium', font_family = 'Century Gothic',text_align = 'left')
#         yag = yagmail.SMTP('demodeepsea@gmail.com', '2WSX@wsx3EDC#edc')
#         yag.send(email, 'CV Classifier', contents='fail mail')
#         pass
#     # requests.post(url, data = myobj)
#     return render_template('home_sender.html',form=form)


#     # response = 'nothing'
#     # response = requests.get('http://localhost:5000/foo')
#     # print(response.content)
#     # data = request.data

#     # return data




# if __name__ == '__main__':
#     app.run(host='localhost',port='3000')
#     # send_mails('g.tsilivis@deepsea.ai')
