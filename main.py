from time import sleep

import pyotp
import qrcode

def generate_secret():
    return pyotp.random_base32();

def generate_totp_url(secret, account_name, issuer):
    return pyotp.totp.TOTP(secret).provisioning_uri(name=account_name, issuer_name=issuer)

def generate_totp(secret):
    return pyotp.TOTP(secret).now();

def print_qrcode_url(url):
    qr = qrcode.QRCode()
    qr.add_data(url)
    qr.make(fit=True)
    qr.print_ascii(invert=True)

secret = generate_secret();
print(generate_totp(secret));
print(f"Secret: {secret}");
user = input("Enter your username: ");
issuer = input("Enter the issuer: ");
totp_url = generate_totp_url(secret, user, issuer);
print(f"TOTP URL: {totp_url}");

# Print QRCode URL for scanning
print_qrcode_url(totp_url);

current_totp = generate_totp(secret);

print(f"Current TOTP: {current_totp}");
while True:
    new_totp = generate_totp(secret);
    if new_totp != current_totp:
        current_totp = new_totp;
        print(f"Current TOTP: {current_totp}");    
    sleep(1);