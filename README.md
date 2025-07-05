# LeetCode Solutions in Python

Этот каталог содержит мои решения задач с [LeetCode](https://leetcode.com/), написанные на Python.

## Структура каталога

```
leetcode/
├── ... .py
├── README.md           # Этот файл
```

## Формат именования файлов

Каждое решение названо в формате:  
`{название_задачи_в_нижнем_регистре}.py`

Пример:  
`two_sum.py` - решение задачи "Two Sum"

## Описание решений

В каждом файле содержится:
1. Решение с минимальными необходимыми комментариями
2. Сложность решения (Big O notation)

### Пример структуры файла:

```python
"""
1. Two Sum
"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []

# Сложность: O(n) по времени, O(n) по памяти
```

## Как использовать

1. Клонируйте репозиторий
2. Перейдите в нужную директорию по уровню сложности
3. Откройте файл с интересующей задачей

## Требования

- Python 3.6+

## Прогресс

![LeetCode Stats](https://leetcard.jacoblin.cool/{lev1nxxx}?theme=nord&font=Roboto&ext=contest) 


