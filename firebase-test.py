# export GOOGLE_APPLICATION_CREDENTIALS="/Users/philippjohn/Developer/youtube-analytics/keys/firebase_key.json"

import toml
import firebase_admin
from firebase_admin import credentials, firestore

# default_app = firebase_admin.initialize_app()

cred = firebase_admin.credentials.Certificate(toml.load(".streamlit/secrets.toml")["firebase_key"])
default_app = firebase_admin.initialize_app(cred, {
	"databaseURL": "https://analytics-44b35.firebaseio.com"
	})

db = firestore.client()

for k in db.collection("videos").get():
    print(k.id, k.to_dict())