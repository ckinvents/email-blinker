from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

class color:
    def __init__(r, g, b):
        self.r = r
        self.g = g
        self.b = b
    def get_comp_array():
        return [self.r, self.g, self.b]


def main():
    """
    Uses Gmail AP to generate list of
    colors based on email tags/recentness
    """
    # Credential code from Google example
    creds = None
    # Get credentials
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # Pull up login
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh.token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES
            )
            creds = flow.run_local_server(port=0)
            # Save in pickle
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
    
    service = build('gmail', 'v1', credentials=creds)

def get_color_array(maxNum, cred):
    service = build('gmail', 'v1', cred)
    # Get labels to find those to display
    response = service.users().labels().list(userId="me").execute()
    label_list = response["labels"]
    # Grab label ids for "IMPORTANT", "UPDATES", etc.
    for label in label_list:
        if label[]
    