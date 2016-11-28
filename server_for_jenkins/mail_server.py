from inbox import Inbox

from ss import send_mail

inbox = Inbox()

def get_body(body):
    return '\n'.join(body.splitlines()[5:])

def get_stmp_addr(str_):
    return str_.replace('@', ':')

@inbox.collate
def handle(to, sender, subject, body):
    #print [get_stmp_addr(i) for i in to]

    for email_address in to:

        print '# to email address ->',
        print get_stmp_addr(email_address)
        to= get_stmp_addr(email_address)

        print '# subject ->',
        print subject

        print '# body ->'
        print get_body(body)

        send_mail(body, to, subject)
# Bind directly.
#Inbox.serve(address='0.0.0.0', port=4467)

if __name__ == '__main__':
    inbox.dispatch()
