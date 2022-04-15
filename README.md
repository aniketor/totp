# totp 
## Time based OTP [![Build Status](https://travis-ci.com/pyizza/totp.svg?branch=main)](https://travis-ci.com/pyizza/totp)
https://tools.ietf.org/html/rfc6238
### Usage


Get time based OTP using given secret and time.
```
get_totp(secret, interval, sha, digits, c_time)
```
secret: base32 encoded string.\
interval: TOTP interval length (Default: 30 secs).\
sha: hashlib digest method (Default: 1).\
digits: output token length (Default: 6).\
c_time: current time (Default: current time).


### Sample
```
from totp import get_totp

SECRET = b'mysupersecretstring000'

result = get_totp(SECRET, 20, 256, 10)
```
"result" will be a 10 digit Time based OTP (SHA256) which will last for 20 secs. 


