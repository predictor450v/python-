import re

text = "The quick brown fox jumps over the lazy dog."

# Search for a pattern
match = re.search("brown", text)
if match:
    print("Match found!")
    print("Start index:", match.start())
    print("End index:", match.end())

