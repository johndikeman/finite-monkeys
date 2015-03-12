import threading,logging,random,string


PARENT = None
NEXT = None
CHANGES = ''
LIST = string.digits + string.ascii_letters + string.punctuation

def work():
    global NEXT
    global CHANGES

    attempt = ''
    while(True):
        if len(CHANGES)==0:
            for c in range(1,random.randint(0,30)):
                attempt+=random.choice(LIST)
            if attempt == NEXT:
                PARENT.reportVictory(attempt)
                logging.debug('found a word!')
            else:
                logging.debug('failed to create a word')

        else:
            NEXT = CHANGES
            CHANGES = ''

class Monkey():
    def __init__(self, parent=None,target=work):
        global PARENT
        self.thread = threading.Thread(target=work)
        PARENT = parent
        logging.debug('monkey awoken.')

    def run(self):
        self.thread.start()

    def updateWord(self,word):
    	global CHANGES 
        CHANGES = word

