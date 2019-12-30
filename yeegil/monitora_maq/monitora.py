# -*- coding: utf-8 -*-
import platform
import psutil
class MonitoraConsumo:
    def server(self):
        self.server = platform.node()
        return self.server
    def memory(self):
        self.memory = psutil.virtual_memory()
        return self.memory[2]
    def cpu(self):
        self.cpu = psutil.cpu_percent()
        return self.cpu