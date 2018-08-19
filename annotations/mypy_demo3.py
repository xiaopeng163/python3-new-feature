from typing import Optional

class Foo:
    def __init__(self, foo_id: int) -> None:
        self.id = foo_id


def get_foo(foo_id: Optional[int]) -> Optional[Foo]:
    if foo_id is None:
        return None
    return Foo(foo_id)


my_foo = get_foo(3)
if my_foo is not None:
    print(my_foo.id)