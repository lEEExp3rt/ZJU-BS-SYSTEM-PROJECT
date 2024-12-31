"""
This file initializes the application package and build global instances.
"""

from app.Configs import Config
from app.database.DatabaseConnector import DatabaseConnector
from app.utils.EmailManager import EmailManager
from app.services.Spider import SpiderManager


''' Global Configuration Instance '''
configs = Config()

''' Global Database Connector Instance '''
db = DatabaseConnector(
    host=configs.db_host,
    port=configs.db_port,
    user=configs.db_user,
    password=configs.db_password,
    database=configs.db_database,
    charset=configs.db_charset
)

''' Global Email Manager Instance '''
email_manager = EmailManager(
    sender_email=configs.email_senderemail,
    sender_name=configs.email_sendername,
    sender_password=configs.email_senderpassword,
    smtp_server=configs.email_smtp,
    smtp_port=configs.email_port
)

''' Global Spider Manager Instance '''
spiders = SpiderManager()
