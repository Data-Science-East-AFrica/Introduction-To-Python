from flask import Flask, render_template, request
from flaskext.mysql import MySQL


app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'MyDB'

mysql = MySQL(app)


@app.route("/")
def index():
  return render_template('index.html')


@app.route('/Contact', methods=['GET', 'POST']) 
def contact():
    if request.method == "POST":
        details = request.form
        FullName = details['fname']
        Email = details['email']
        Message = details['message']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO MyUsers(FullName, Email, Message) VALUES (%s, %s, %s)", (FullName, Email, Message))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 5000, debug = True)