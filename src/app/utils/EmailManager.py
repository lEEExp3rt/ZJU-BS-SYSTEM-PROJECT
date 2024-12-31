"""
This module manages the emails.
"""

import re
import smtplib
import random
from email.mime.text import MIMEText


def validate_email(email: str) -> bool:
    """
    Validate the email format.

    :param email: The email to be validated.

    :return: True if the email is valid, False otherwise.
    """

    return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email) is not None

def generate_verification_code(length: int = 6) -> str:
    """
    Generate a random verification code.

    :param length: The length of the verification code. Default is 6.

    :return: The generated verification code.
    """

    return ''.join(random.choices('0123456789', k=length))

class EmailManager:
    """
    The email manager class to handle sending emails.
    """

    def __init__(self, sender_email: str, sender_name: str, sender_password: str, smtp_server: str, smtp_port: int = 465):

        self.__smtp_server = smtp_server
        self.__smtp_port = smtp_port
        self.__sender_email = sender_email
        self.__sender_name = sender_name
        self.__sender_password = sender_password

    def send(self, receiver_email: str, content: str, receiver_name: str = None, subject: str = None, charset: str = 'utf-8'):
        """
        Send an email to the receiver.

        :param receiver_name: The name of the receiver.
        :param receiver_email: The email of the receiver.
        :param subject: The subject of the email.
        :param content: The content of the email.
        :param charset: The charset of the email. Default is 'utf-8'.
        """

        def format_name(email: str, name: str = None) -> str:
            """
            Format the name to be used in the email.
            """

            return (name.replace(' ', '_') if name is not None else email.split('@')[0]) + f' <{email}>'

        message = MIMEText(content, 'plain', charset)
        message['From'] = format_name(self.__sender_email, self.__sender_name)
        message['To'] = format_name(receiver_email, receiver_name) + ',' + message['From']
        message['Subject'] = subject

        try:
            smtp_obj = smtplib.SMTP_SSL(self.__smtp_server, self.__smtp_port) # Connect to the SMTP server.
            smtp_obj.login(self.__sender_email, self.__sender_password) # Login to the SMTP server.
            smtp_obj.sendmail(
                from_addr=self.__sender_email,
                to_addrs=[receiver_email, self.__sender_email],
                msg=message.as_string()
            )
            smtp_obj.quit() # Quit the SMTP server.
        except smtplib.SMTPException as e:
            raise e
