from decouple import config
import platform
import psutil
import smtplib


SERVER = config('SERVER')
PORT = config('PORT')
FROM = config('SENDER_MAIL')
SUBJECT = 'Yeegil - Message.'
TO = 'Recebe uma lista emails vindas do banco de dados'

class ComsumptionMonitor:
    """
    Classe responsável por realizar a captura das informações do servidor.
    """
    def server():  # pylint: disable=no-method-argument
        server = platform.node()

        return server

    def memory():  # pylint: disable=no-method-argument
        memory = psutil.virtual_memory()

        return memory[2]

    def cpu():  # pylint: disable=no-method-argument
        cpu = psutil.cpu_percent()

        return cpu


class SendMail:
    """
    Classe responsável por manipular e enviar emails com informativos do sistema.
    """
    def message_send(maq,memo,cpu):  # pylint: disable=no-self-argument
        message = '''From: %s\r\nTo: %s\r\nSubject: %s\r\n

        %s
        %s
        %s
        ''' % (FROM, ", ".join(TO), SUBJECT, maq,memo,cpu)

        server =  smtplib.SMTP(SERVER, 25)
        server.sendmail(FROM,TO,message)
        server.quit()
