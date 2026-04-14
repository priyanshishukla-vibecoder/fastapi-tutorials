import pickle 
from pathlib import Path

import streamlit_authenticator as stauth

names=["Priyanshi Shukla","Arjun Gupta"]
usernames=["priyanshi","arjun"]
passwords=["12345","54321"]
# hashed_passwords=stauth.Hasher(passwords).generate()

hashed_passwords = [stauth.Hasher().hash(p) for p in passwords]
file_path=Path(__file__).parent/"hashed_pw.pkl"

# Save the hashed passwords to a file
with file_path.open('wb') as f:
    pickle.dump(hashed_passwords, f)