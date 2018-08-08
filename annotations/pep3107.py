"""
PEP:	3107
Title:	Function Annotations
Author:	Collin Winter <collinwinter at google.com>, Tony Lownds <tony at lownds.com>
Status:	Final
Type:	Standards Track
Created:	2-Dec-2006
Python-Version:	3.0
Post-History:	
"""

def sum(x: "num", y: int) -> int:
    """
    :param x: int
    :param y: int
    :param return: int
    """
    return x + y


if __name__ == "__main__":
    x = 10
    y = 20
    print(f'{x} + {y} = {sum(x, y)}')
    print(sum.__annotations__)