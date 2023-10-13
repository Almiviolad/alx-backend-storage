import requests

# Your username and password
username = 'alohmv.19@student.funaab.edu.ng'
password = 'almiviolad7$'

# Create a session to handle cookies
session = requests.Session()

# Perform a POST request to authenticate
login_url = 'https://intranet.alxswe.com/auth/sign_in'
# Replace with the actual login page URL
payload = {'username': username, 'password': password}
session.post(login_url, data=payload)

# Now you can access the protected resource
resource_url = 'https://intranet.alxswe.com/rltoken/uPn947gnZLaa0FJrrAFTGQ'  # Replace with the actual resource URL
response = session.get(resource_url)

# Save the content to a file
with open('downloaded_file.zip', 'wb') as file:
    file.write(response.content)
