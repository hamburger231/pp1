import re

message = "To be, or not to be, that is the question"
print(len(re.findall("[aeiouAEIOU]",message)))