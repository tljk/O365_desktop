from O365 import Account, MSOffice365Protocol
import os

class OAuth(Account):
    def __init__(self):
        credentials = ('', '')

        protocol = MSOffice365Protocol()
        super().__init__(credentials, protocol=protocol)

        if 'o365_token.txt' not in os.listdir():
            self.account.authenticate(scopes=['basic', 'calendar_all', 'tasks_all'])