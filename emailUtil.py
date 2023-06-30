import myImapClient
import email

class emailUtil:
    '''Use myImapClient to fetch and format emails'''
    def __init__(self, myImapClient, targetEmail, targetSubject, targetFooterSize):
        self.__myImapClient = myImapClient
        self.__targetEmail = targetEmail
        self.__targetSubject = targetSubject
        self.__targetFooterSize = targetFooterSize

    def getEmail(self):
        '''get the last mail you received by targetEmail with targetSubject'''
        try:
            self.__myImapClient.login()
            print("getting email...")
            imapClient = self.__myImapClient.getClient()
            imapClient.select_folder('INBOX')
            emails = imapClient.search(['FROM', self.__targetEmail, 'SUBJECT', self.__targetSubject])
            print("\tfounded!")
            return imapClient.fetch(emails, ['RFC822']).items()

        except Exception:
            print("connection aborted!")

        finally:
            self.__myImapClient.logout()
    
    def formatEmail(self, userEmail):
        '''create a Human-readable message from userEmail and removing targetFooterSize characters from the end'''
        print("formatting email...")
        for _, emailData in userEmail:
            rawEmail = emailData[b'RFC822']
            emailMessage = email.message_from_bytes(rawEmail)

            emailContent = ""
            if emailMessage.is_multipart():
                for part in emailMessage.walk():
                    if part.get_content_type() == 'text/plain':
                        email_content = part.get_payload(decode=True).decode('utf-8')
                        break
            else:
                if emailMessage.get_content_type() == 'text/plain':
                    email_content = emailMessage.get_payload(decode=True).decode('utf-8')
        
        print("\tformatted!")
        return email_content[:len(email_content)-self.__targetFooterSize]