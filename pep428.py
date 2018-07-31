"""
PEP 428 -- The pathlib module -- object-oriented filesystem paths
PEP:	428
Title:	The pathlib module -- object-oriented filesystem paths
Author:	Antoine Pitrou <solipsis at pitrou.net>
Status:	Final
Type:	Standards Track
Created:	30-July-2012
Python-Version:	3.4
Post-History:	https://mail.python.org/pipermail/python-ideas/2012-October/016338.html
Resolution:	https://mail.python.org/pipermail/python-dev/2013-November/130424.html
"""

from pathlib import Path

# basic
print('current file path:', Path(__file__).absolute())
print('current run  path:', Path('.').absolute())

# file find 