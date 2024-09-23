# 11reemailcheck.py =>나중에 할것.

import re

def email_check(email):
    pass
    # re.findall('^시작,[a-z]{2,}',) ^ 시작을 의미  $끝
    # re.findall(' ',[^a-z]{2,}',)   []에 ^이 들어가면 부정의 의미임.

email_check("kim@gmail") # .org   .kr   .com   .net
email_check("kim@gmail.net") # @포함여부
email_check("$^kim") #첫글자가 특수문자 포함
email_check("kim@gmail.net") #올바른 이메일입니다.
