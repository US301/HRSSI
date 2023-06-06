from flask import Flask, render_template, request, flash
from flask_mail import Mail, Message


app = Flask(__name__)
app.secret_key = "301856"
# Sending email/contact/newsletters

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'usamasaid321@gmail.com'
app.config['MAIL_PASSWORD'] = 'XXXXXXXXXXXXXXXXXX'

mail = Mail(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


# @app.route('/services')
# def services():
#     return render_template('services.html')


@app.route('/contact', methods=['POST','GET'])
def contact():
    if request.method == 'POST':
        name = request.form.get("name")
        message = request.form.get("message")
        email = request.form.get("email")
        subject = request.form.get("subject")
        msg = Message(subject, sender=f'{email}', recipients=['hrssi.com@gmail.com'])
        msg.body = f'''
        Name: {name}
        Email: {email}
        Message: {message}
        '''.format(name, email, message)
        mail.send(msg)
        flash('Your message has been sent!')
    return render_template('contact.html')


@app.route('/donation')
def donation():
    return render_template('donation.html')


@app.route('/join')
def newsletter():
    return render_template('join.html')


if __name__ == '__main__':
    app.run(debug=True)
