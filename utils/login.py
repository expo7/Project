import pyotp
import robin_stocks as rs
def sign_in():
    totp  = pyotp.TOTP("X332CR3PQSYGYOF7").now()
    rs.robinhood.login(username='bsavelli66@gmail.com', password='Canyon6687',expiresIn=86400,scope='internal',store_session=True,mfa_code=totp)

account=sign_in()
print('robinhood login')
