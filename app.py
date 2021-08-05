from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'nahvandiemen@gmail.com'
app.config['MAIL_PASSWORD'] = 'N@#umvd98'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route('/home', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = Message('Hello Message', sender='nahvandiemen@gmail.com', recipients=['vandiemennahum@gmail.com'])
        msg.body = "This is the email you received from the flask email meaning its a test"
        mail.send(msg)
        return "Send email"
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run(port=5001)
