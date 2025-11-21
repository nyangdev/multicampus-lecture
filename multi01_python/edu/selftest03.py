import re

# 다음 텍스트에서 이메일 추출하기


text = "내 이메일 주소 example@email.com 이야. 여기로 연락줘"

"""
출력 결과 : 
['example@email.com']
"""

extract = re.search(r"[a-z]*@[a-z]*.[a-z]*", text)
print(extract.group(0))