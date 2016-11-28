from inbox import Inbox

inbox = Inbox()

@inbox.collate
def handle(to, sender, subject, body):
    print to

    print sender

    print subject
    print body

if __name__ == '__main__':
    inbox.dispatch()
