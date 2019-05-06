from datetime import datetime
today = datetime.today().strftime('%D')
# print(today)

class PythonProjects():

    def __init__(self,msg):
        self.msg = msg
        self.say_it()   # Date

    def say_it(self):
        print(self.msg)

class utilities(PythonProjects):

    def say_it(self):
        print(self.msg + ' @ ' + today)     # Date @ 05/06/19

if __name__ == '__main__':

    msg = 'Date'
    instPP = PythonProjects(msg)

    instU = utilities(msg)
    # instU.say_it()