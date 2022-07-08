import base64
import hashlib
from Crypto.Cipher import AES
from Crypto import Random

BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(
    BLOCK_SIZE - len(s) % BLOCK_SIZE
)
unpad = lambda s: s[: -ord(s[len(s) - 1 :])]

key = "idontknow"
cipher = b"dtnrGf+mqpVpCUjN1FUIgai7H0TPNs62LvWEoOLCzukCQiPZBgYNKv7B+ety0JTQ"
flag = ""


def encrypt(plain_text, key):
    private_key = hashlib.sha256(key.encode("utf-8")).digest()
    plain_text = pad(plain_text)
    print("After padding:", plain_text)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(plain_text))


def decrypt(cipher, key):
    # your code
    pass


if __name__ == "__main__":
    print(decrypt(cipher, key))
