import json
import re

a=json.loads(input())

pattern=r"^@[a-z]*_[a-z_]*$"

for u in a:
    if re.match(pattern, u["handle"]):
        print(u["user_id"])