"""
This is a test suite for email module.
"""

from backend.utils.EmailManager import EmailManager
from backend.Configs import Config

def test_send_email():
    """
    Test sending email.
    """

    config = Config()
    email_manager = EmailManager(
        sender_email=config.email_senderemail,
        sender_name=config.email_sendername,
        sender_password=config.email_senderpassword,
        smtp_server=config.email_smtp,
        smtp_port=config.email_port
    )

    email_manager.send(
        receiver_email='1838782855@qq.com',
        content='This is a test email 1.'
    )

    email_manager.send(
        receiver_email='1838782855@qq.com',
        content='This is a test email 2.',
        subject='Test Email'
    )

    email_manager.send(
        receiver_email='1838782855@qq.com',
        content='This is a test email 3.',
        subject='Test Email',
        receiver_name='!EEExp3rt'
    )

    print("Email test passed.")


if __name__ == '__main__':
    test_send_email()