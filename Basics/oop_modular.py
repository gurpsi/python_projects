class to_print():

    def __init__(self,msg):
        self.msg = msg
        self.say_anything()  # We can call the function as soon as it initialises the value.

    def say_anything(self):
        print(self.msg)

if __name__ == '__main__':
    print("Hi there ")

    inst = to_print("This is the message")
    inst.say_anything()

'''
with the above statement if __name__ == '__main__':
if the module get's imported everything below this line will not be executed.

This is a great way to test each module.


We define def __init__ so that all of the other definition can now access all the initialised variables.  
'''

