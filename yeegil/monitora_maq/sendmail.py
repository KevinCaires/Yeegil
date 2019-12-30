import smtplib
SERVER = "webmail.exemplo.com.br"
FROM = "aplicacoes@exemplo.com.br"
TO = ["joao.da.silva@exemplo.com.br"]
SUBJECT = 'Yeegil - Monitor de consumo'

def message_send(maq,memo,cpu):
    message = """From: %s\r\nTo: %s\r\nSubject: %s\r\n
    
    %s
    %s
    %s
    """%(FROM, ", ".join(TO), SUBJECT, maq,memo,cpu)

    server =  smtplib.SMTP(SERVER, 25)
    server.sendmail(FROM,TO,message)
    server.quit()