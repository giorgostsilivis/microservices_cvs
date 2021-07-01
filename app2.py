from flask import Flask
import pandas as pd
from pretty_html_table import build_table
import sqlite3
import sqlalchemy



app = Flask(__name__)

@app.route('/return_message')
def return_message():
    # d = {'col1': [1, 2], 'col2': [3, 4]}
    # df = pd.DataFrame(data=d)
    USER = ''
    cnx = sqlite3.connect('db.sqlite')
    df = pd.read_sql_query("SELECT * FROM class_table", cnx)
    cnx.close()
    # return 'the message'
    html_table_blue_light = build_table(df[df['Class']=='A CLASS'], 'green_light')
    html_table_red_light = build_table(df[df['Class']=='B CLASS'], 'red_light')
    html_table_grey_light = build_table(df[df['Class']=='UNKNOWN CLASS'], 'grey_light')
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
    return start+html_table_blue_light+html_table_red_light+html_table_grey_light+end

if __name__ == '__main__':
    app.run(host='localhost',port='4000')


# if __name__ == '__main__':
#     app.run(debug=True)
