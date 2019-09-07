'''
Playing around with datetime.
'''

from datetime import datetime
today = datetime.now().strftime("%D")

class python_project():

    def __init__(self, msg):
        self.msg = msg
        self.print_msg()

        # Creating the instance of the second class:
        inst2 = utilities()
        inst2.print_msg_with_time(msg)


    def print_msg(self):
        print(self.msg)

class utilities():
    def print_msg_with_time(self,msg):
        print(msg + '@ ' + today)

if __name__ == '__main__':
    inst1 = python_project("Hello there back ")
