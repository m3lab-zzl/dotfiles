import getpass
import os
import smtplib
from argparse import ArgumentParser
from email.header import Header
from email.mime.text import MIMEText

this_dir = os.path.dirname(os.path.abspath(__file__))

ap = ArgumentParser("mail yourself")
ap.add_argument("-t", "--title", help="title")
ap.add_argument("-c", "--content", help="content")
args = ap.parse_args()

passwd = getpass.getpass("password:")


def send_email(subject, message, from_addr, to_addr, smtp_server, port, password):
    msg = MIMEText(message, "plain", "utf-8")
    msg["From"] = Header(from_addr)
    msg["To"] = Header(to_addr)
    msg["Subject"] = Header(subject)

    server = smtplib.SMTP_SSL(smtp_server, port)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()


send_email(
    subject=args.title,
    message=args.content,
    from_addr="Deelin221zzl@163.com",  # <---
    to_addr="1091749869@qq.com",  # <---
    smtp_server="smtp.163.com",
    port=465,
    password=passwd,
)
