from cryptography.fernet import Fernet
import base64

key = Fernet.generate_key()

def encrypt(txt):

        txt = str(txt)
        cipher_suite = Fernet(key)
        encrypted_text = cipher_suite.encrypt(txt.encode('ascii'))
        encrypted_text = base64.urlsafe_b64encode(encrypted_text).decode("ascii")
        return encrypted_text


def decrypt(txt):

        txt = base64.urlsafe_b64decode(txt)
        cipher_suite = Fernet(key)#(settings.ENCRYPT_KEY)
        decoded_text = cipher_suite.decrypt(txt).decode("ascii")
        return decoded_text