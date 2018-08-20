
import sys
import locale

print('system default encoding: {}'.format(sys.getdefaultencoding()))
print('file system encoding: {}'.format(sys.getfilesystemencoding()))
print('system current encoding: {}'.format(locale.getdefaultlocale()))
print('system standard input encoding: {}'.format(sys.stdin.encoding))
print('system standard output encoding: {}'.format(sys.stdout.encoding))

a = '中国'
b = a.encode('utf-8')
print(a, b)
