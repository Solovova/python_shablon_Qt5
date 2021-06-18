import subprocess
import threading
 
class ThreadMain(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        

    # def __init__(self, number, logger):
    #     threading.Thread.__init__(self)
    #     self.number = number
    #     self.logger = logger
    def runScript(self):
        # , stdout=subprocess.STDOUT
        scrname = "C:\\prg\\python_shablon_Qt5\\scripts\\test.ps1"
        p = subprocess.Popen(['powershell.exe', scrname])
        stdoutdata, stderrdata = p.communicate()

 
    def run(self):
        """
        Run the thread
        """
        self.runScript()
        # logger.debug('Calling doubler')
        # doubler(self.number, self.logger)
 
 
    # def get_logger():
    #     logger = logging.getLogger("threading_example")
    #     logger.setLevel(logging.DEBUG)
 
    #     fh = logging.FileHandler("threading_class.log")
    #     fmt = '%(asctime)s - %(threadName)s - %(levelname)s - %(message)s'
    #     formatter = logging.Formatter(fmt)
    #     fh.setFormatter(formatter)
 
    #     logger.addHandler(fh)
    #     return logger