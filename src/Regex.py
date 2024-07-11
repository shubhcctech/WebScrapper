import re

pattern =r"[()]"
str = "Redmi 13C (Stardust Black, 6GB RAM, 128GB Storage) | Powered by 4G MediaTek Helio G85 | 90Hz Display | 50MP AI Triple Camera"
op = re.search(pattern,str)

if op:
    print("JOD")
