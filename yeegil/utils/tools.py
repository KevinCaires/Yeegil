from decouple import config
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import platform
import psutil
import smtplib


SERVER = config('SERVER')
PORT = config('PORT')
FROM = config('SENDER_MAIL')
PASSWORD = config('MAIL_PASSWORD')
SUBJECT = config('SUBJECT')


class ComsumptionMonitor:
    """
    Classe responsável por realizar a captura das informações do servidor.
    """
    def server():  # pylint: disable=no-method-argument
        server = platform.node()

        return server

    def memory():  # pylint: disable=no-method-argument
        memory = psutil.virtual_memory()

        return (memory[2] + '%')

    def cpu():  # pylint: disable=no-method-argument
        cpu = psutil.cpu_percent()

        return cpu


class SendMail:
    """
    Classe responsável por manipular e enviar emails com informativos do sistema.
    """
    def message_send(server, memory, cpu):  # pylint: disable=no-self-argument
        # create message object instance
        msg = MIMEMultipart()
        
        # setup the parameters of the message
        password = PASSWORD
        msg['From'] = FROM
        msg['To'] = 'kevincaires@icloud.com'
        msg['Subject'] = SUBJECT
        
        message = f'''
        SERVER: {server}
        MEMORY: {memory}
        CPU: {cpu}
        '''

        # add in the message body
        msg.attach(MIMEText(message, 'plain'))
        
        #create server
        server = smtplib.SMTP(f'{SERVER}:{PORT}')
        
        server.starttls()
        
        # Login Credentials for sending the mail
        server.login(msg['From'], password)
        
        
        # send the message via the server.
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        
        server.quit()
