from flask import Flask, render_template, request
import smtplib # used to connect to mail server.
import config # importing the config.py file in order to use the login credentials.
from email.message import EmailMessage # Class EmailMessage.

# creating an instance of the Flask object.
app = Flask(__name__)
app.config['SECRET_KEY'] = 'eliasfara'

# App routing is used to map the specific URL.
# It is used to access MailServer.html webpage.
@app.route('/')
def index():
    title = "Mail Server"

    # This method is used to render the MailServer.html template and to pass the title variable to the template engine.
    return render_template("MailServer.html", title=title)

# It is used to access form.html webpage.
@app.route('/form', methods=["POST"])
def form():
    title = "Thank You!"
    email = request.form.get("email") # Obtaining the email value from the MailServer.html after the submissoin is successful.
    subject = request.form.get("subject") # Obtaining the subject value from the MailServer.html after the submissoin is successful.
    message = request.form.get("message") # Obtaining the message value from the MailServer.html after the submissoin is successful.

    # Creating a new email message.
    Mymessage = EmailMessage() 
    Mymessage['Subject'] = subject # Setting up the email subject.
    Mymessage['From'] = config.MyEmail # Sender
    Mymessage['To'] = email # Receiver
    Mymessage.set_content(message) # Passing in the content of the message.


    # smtp.gmail.com: Gmail Mail Server.
    # 465: Port Number.
    # conn: Connection variable name.
    # Used smtplib.SMTP_SSL to create the client object.
    # Which uses a secure encrypted SSL protocol to connect to the SMTP server
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as conn:
        conn.login(config.MyEmail, config.MyPass) # An smtp object has a method login that allows you to authenticate with an email server.
        conn.send_message(Mymessage) # Passing in the content of the email.
        conn.quit() #To terminate the connection between the client and the SMTP server.

    # This method is used to render the form.html template and to pass the title and the email variables to the template engine.
    return render_template("form.html", title=title, email=email)