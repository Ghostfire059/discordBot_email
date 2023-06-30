import imapclient

class myImapClient:
    '''Create client needed to log and get mails'''
    def __init__(self, imap, username, password):
        self.__IMAPSERVER = imap
        self.__USERNAME = username
        self.__PASSWORD = password
        self.__imapClient = imapclient.IMAPClient(self.__IMAPSERVER)

    def login(self):
        print("logging to " +self.__IMAPSERVER.replace('imap.', '')+ "...")
        self.__imapClient.login(self.__USERNAME, self.__PASSWORD)
        print("\tlogged in!")

    def logout(self):
        print("logout from " +self.__IMAPSERVER.replace('imap.', '')+ "...")
        self.__imapClient.logout()
        print("\tlogged out!")

    def getClient(self):
        return self.__imapClient