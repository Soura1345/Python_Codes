n: int = 5

name : str = "Soura"

def sum(a,b) -> int:
    return a + b

print(sum(1,3))

from typing import List, Union, Dict, Tuple

numbers: List[int] = [1,2,3,4,5]

person: Tuple[str, int] = ("Soura", 13)

scorce: Dict[str, int] = {"Soura":13, "Pal":4}

identifier: Union[int, str] = "OD28KSH"
identifier = 123345