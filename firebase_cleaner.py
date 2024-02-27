import requests
import firebase_admin
from firebase_admin import credentials, auth, db
from datetime import datetime

# 12 am , 12 pm, 2 am, 2 pm
def sign_in_with_email_and_password(email, password):
    # Firebase Authentication Sign In URL
    sign_in_url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"

    # Your Firebase project API key
    api_key = "AIzaSyARCqBKsGpsuuyqg1c8dJtvDngqajHSITo"

    # Construct the request payload
    payload = {
        "email": 'wintersolstudios@gmail.com',
        "password": password,
        "returnSecureToken": True
    }

    # Make the request to sign in
    response = requests.post(f"{sign_in_url}?key={api_key}", json=payload)

    # Check for errors
    if response.status_code == 200:
        # Successful sign in
        return response.json()
    else:
        # Error occurred
        print(f"Error: {response.status_code}, {response.json()}")
        return None

# Replace with your own email and password
email = "wintersolstudios@gmail.com"
password = "Shivam@15"

result = sign_in_with_email_and_password(email, password)

if result:
    print(f"Successfully signed in. User ID: {result['localId']}, ID Token: {result['idToken']}")
else:
    print("Sign-in failed.")

# Initialize Firebase Admin SDK
cred = credentials.Certificate("lmaoochat-firebase-adminsdk-66hc4-e792de1047.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://lmaoochat-default-rtdb.firebaseio.com/'})

def delete_data(path):
    # Reference to the user's data in the database
    user_ref = db.reference(f'{path}')

    # Write data to the user's node
    user_ref.delete()

def write_data(path):
    user_ref = db.reference(path=path)
    user_ref.update({'hi':'hahaha'})

# Replace 'your_id_token' with the actual ID token received from the client
id_token = result['idToken']

# Get the current date and time
current_datetime = datetime.now()

# Extract the current hour
current_hour = current_datetime.hour

try:
    # Verify the ID token
    decoded_token = auth.verify_id_token(id_token)

    # Obtain the UID from the decoded token
    uid = decoded_token['uid']

    # Read data from the user's node
    if current_hour == 0:
        delete_data(path='')
    elif current_hour == 2:
        delete_data(path='')
    elif current_hour == 14:
        write_data(path='chat_testing')
    elif current_hour == 19:
        write_data(path='chat_testing')
    # have to add for 12 noon

except auth.AuthError as e:
    print(f"Error verifying ID token: {e}")
