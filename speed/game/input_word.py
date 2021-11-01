import time
from threading import Thread
class InputWord:
    """This part processes the input.
    
    Stereotype:
        Information Holder

    """
    def input(self):
        answer = None
        def check():
            time.sleep(2)
            if answer != None:
                return
            else:
                late = "Too Slow, press enter"
                return print(late)
            
        Thread(target = check).start()
        answer = input("Input something: ")
        return answer