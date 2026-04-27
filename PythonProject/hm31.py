import re

text = "The events N 123456 happened on 15/03/2025, 01.12.2024 and 09-09-2023. Deadline: 28/02/2022."


result = re.finditer(r"\d{2}/\d{2}/\d{4}|\d{2}\.\d{2}\.\d{4}|\d{2}-\d{2}-\d{4}", text)

for res in result:
    print(res.group())


import re


tag_input = "python, data-science / machine-learning; AI  neural-networks"


tags = re.split(r'[ ,;/]+', tag_input)

result = [tag.strip() for tag in tags if tag.strip()]

print(result)