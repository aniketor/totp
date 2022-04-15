#!/usr/bin/env python3

import unittest

from totp import get_totp


class TestTOTP(unittest.TestCase):
    def test_totp(self):
        """
        Test 6 digit TOTP for SHA1, SHA224, SHA256, SHA384, SHA512
        """
        SECRET = b'TESTINGtotp@github123'
        TIME = 1621624446
        MAP = {1:543808, 224:981643, 256:965830, 384:167126, 512:750133}
        for key in MAP:
            result = get_totp(SECRET, 30, key, 6, TIME)
            self.assertEqual(int(result), MAP[key])

if __name__ == '__main__':
    unittest.main()

# End.
