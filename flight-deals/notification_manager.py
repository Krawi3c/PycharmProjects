from twilio.rest import Client
import smtplib

TWILIO_SID = 'AC3d1bf4faa7a08e15c8bae6afa06f2fc5'
TWILIO_AUTH_TOKEN = '495ac29417777e6b837ebbf795ab941a'
TWILIO_VIRTUAL_NUMBER = "+12707137151"
TWILIO_VERIFIED_NUMBER = "+48730342138"
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "Krawiec2001k@gmail.com"
MY_PASSWORD = "ojhhkgjdhrrjzppq"

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )