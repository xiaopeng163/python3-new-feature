# -*- coding: utf-8 -*-

import sys
import locale

print 'system default encoding: {}'.format(sys.getdefaultencoding())
print 'file system encoding: {}'.format(sys.getfilesystemencoding())
print 'system current encoding: {}'.format(locale.getdefaultlocale())
print 'system standard input encoding: {}'.format(sys.stdin.encoding)
print 'system standard output encoding: {}'.format(sys.stdout.encoding)

a = '中国'
b = b'中国'
c = '\xe4\xb8\xad\xe5\x9b\xbd'
print a
print repr(b)
print a == b
print a == c
