from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# class color:
#     def __init__(r, g, b):
#         self.r = r
#         self.g = g
#         self.b = b
#     def get_comp_array():
#         return [self.r, self.g, self.b]

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def get_colors():
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
        if creds and creds.expired and creds.refresh_token:
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
    # Get labels to find those to display
    label_response = service.users().labels().list(userId="me").execute()
    label_list = label_response["labels"]
    # Grab all emails
    message_list = []
    pageQuery = None
    while len(message_list) < 60:
        message_response = service.users().messages().list(userId="me", labelIds=["UNREAD"], q=pageQuery).execute()
        message_list.extend(message_response["messages"])
        pageQuery = message_response["nextPageToken"]
    color_list = []
    for i in range(0, 60):
        message = service.users().messages().get(userId="me", id=message_list[i]["id"]).execute()
        label = message["labelIds"]
        if "IMPORTANT" in label:
            color_list.append("red")
            print("IMPORTANT")
        elif "CATEGORY_PERSONAL" in label:
            color_list.append("green")
            print("SOCIAL")
        elif "CATEGORY_UPDATES" in label:
            color_list.append("orange")
            print("UPDATE")
        elif "CATEGORY_SOCIAL" in label:
            color_list.append("yellow")
            print("SOCIAL")
        elif "CATEGORY_FORUMS" in label:
            color_list.append("blue")
            print("FORUM")
        else:
            color_list.append("white")
    for color in color_list:
	print(color)
    return color_list
        

if __name__ == '__main__':
    main()
