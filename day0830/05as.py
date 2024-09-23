#05as.py

import datetime as dt #모듈명을 dt로 짧게 별칭부여 가능
import math
import re #정규식
import sys 

my = dt.datetime.now() 
print('날짜 및 시간 ',my) #날짜 및 시간  2024-08-30 11:22:38.014312

print()
print(dir(math)) #math모듈의 경로를 확인
print()
print(dir(re))
print()
'''
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 
'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 
'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 
'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs',
 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 
 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'sumprod', 'tan', 'tanh', 'tau', 'trunc', 'ulp']

['A', 'ASCII', 'DEBUG', 'DOTALL', 'I', 'IGNORECASE', 'L', 'LOCALE',
 'M', 'MULTILINE', 'Match', 'NOFLAG', 'Pattern', 'RegexFlag', 'S', 
 'Scanner', 'T', 'TEMPLATE', 'U', 'UNICODE', 'VERBOSE', 'X', '_MAXCACHE', '_MAXCACHE2', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_cache', '_cache2', '_casefix', '_compile', '_compile_template', '_compiler', '_constants', '_parser', '_pickle', '_special_chars_map', '_sre', 'compile', 'copyreg', 'enum', 'error', 'escape', 'findall', 'finditer', 'fullmatch', 'functools', 'match', 'purge', 'search', 'split', 'sub', 'subn', 'template']
PS C:\Mnet\workPython>
'''
print('prefix 가상이름',sys.prefix) #다양한 속성명 확인
print('version 버전이름',sys.version) #sys의 버전
print('copyright 소유',sys.copyright)
print()
print('path 경로',sys.path)
'''
 Copyright (c) 1995-2001 Corporation for National Research Initiatives.
All Rights Reserved.

Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
All Rights Reserved.

path 경로 ['c:\\Mnet\\workPython\\day0830', 'C:\\Users\\user\\anaconda3\\envs\\ck\\python312.zip', 'C:\\Users\\user\\anaconda3\\envs\\ck\\DLLs', 'C:\\Users\\user\\anaconda3\\envs\\ck\\Lib', 'C:\\Users\\user\\anaconda3\\envs\\ck', 'C:\\Users\\user\\anaconda3\\envs\\ck\\Lib\\site-packages', 'C:\\Users\\user\\anaconda3\\envs\\ck\\Lib\\site-packages\\win32', 'C:\\Users\\user\\anaconda3\\envs\\ck\\Lib\\site-packages\\win32\\lib', 'C:\\Users\\user\\anaconda3\\envs\\ck\\Lib\\site-packages\\Pythonwin']
PS C:\Mnet\workPython>
 '''
