
from typing import List, Any

def join_data_elements(elements: List[Any]) -> str:

    return " | ".join(str(item) for item in elements)


data = [42, "hello", [1, 2, 3], {"a": 1, "b": 2}]
print(join_data_elements(data))

from typing import List, Dict, Union


def calculate_total_score(users: List[Dict[str, Union[str, List[int]]]]) -> int:

    total = 0
    for user in users:

        total += sum(user.get("scores", []))
    return total



data = [
    {"name": "Alice", "scores": [10, 20, 30]},
    {"name": "Bob", "scores": [5, 15, 25]},
    {"name": "Charlie", "scores": [7, 17, 27]}
]

result = calculate_total_score(data)
print(f"Итоговый балл: {result}")