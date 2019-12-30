# -*- coding: utf-8 -*-
import monitora
import time
import sendmail
while True:
    report = monitora.MonitoraConsumo()
    memory = report.memory()
    cpu = report.cpu()
    if memory or cpu >= 80:
        maquina = ('Server: ', report.server())
        ram = 'Memória: %s'%(memory)
        processador = 'CPU: %s'%(cpu)
        sendmail.message_send(maquina,ram,processador)
    time.sleep(10)