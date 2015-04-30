import imaplib
import sys

obj = imaplib.IMAP4_SSL('outlook.office365.com','993')
obj.login(sys.argv[1],sys.argv[2])
obj.select()
print len(obj.search(None, 'UnSeen')[1][0].split())
