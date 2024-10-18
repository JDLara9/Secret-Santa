import smtplib

def send_sms_via_email(phoneNum, message, carrier_gateway):
    to = f"{phoneNum}@{carrier_gateway}"
    from_email = "automation.email110@gmail.com"
    password = "oyit nxcm ryyi wynm"

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to, message)

send_sms_via_email('7135779932', 'Hello', 'tmomail.net')