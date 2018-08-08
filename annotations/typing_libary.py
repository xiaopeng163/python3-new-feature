"""
typing library
"""
from typing import List, Dict, Tuple, Optional

# for List
students: List[str] = ['A', 'B', 'C']
years: List[int] = [2001, 2002, 2003]
numbers: List[List[int]] = [[1, 2, 3], [4, 5, 6]]

# for tuple
connection: Tuple[str, int] = ('10.10.10.10', 80)

# Type aliases
Address = Tuple[str, int]

address: Address = ('1.1.1.1', 80)


def connect(param: List[Address]) -> bool:
    param.


# Any

def hash_b(item: Any) -> int:
    pass



