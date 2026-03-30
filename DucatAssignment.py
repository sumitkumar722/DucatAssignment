# Python String Methods #

# 1. lower()
# Convert to lowercase
"HELLO".lower()  # 'hello'

# 2. upper()
# Convert to uppercase
"hello".upper()  # 'HELLO'

# 3. title()
# Capitalize each word
"hello world".title()  # 'Hello World'

# 4. capitalize()
# Capitalize first letter
"hello".capitalize()  # 'Hello'

# 5. swapcase()
# Swap upper - lower
"HeLLo".swapcase()  # 'hEllO'

# 6. strip()
# Remove spaces both sides
"  hi  ".strip()  # 'hi'

# 7. lstrip()
# Left trim
"  hi".lstrip()  # 'hi'

# 8. rstrip()
# Right trim
"hi  ".rstrip()  # 'hi'

# 9. replace()
# Replace substring
"hello".replace("l", "x")  # 'hexxo'

# 10. find()
# Return index or -1
"hello".find("e")  # 1

# 11. index()
# Like find but error if not found
"hello".index("e")  # 1

# 12. count()
# Count occurrences
"hello".count("l")  # 2

# 13. startswith()
# Check start
"hello".startswith("he")  # True

# 14. endswith()
# Check end
"hello".endswith("lo")  # True

# 15. split()
# Split into list
"a,b,c".split(",")  # ['a', 'b', 'c']

# 16. rsplit()
# Split from right
"a-b-c".rsplit("-", 1)  # ['a-b', 'c']

# 17. splitlines()
# Split by lines
"a\nb".splitlines()  # ['a', 'b']

# 18. join()
# Join list into string
",".join(["a", "b"])  # 'a,b'

# 19. isalpha()
# Only letters
"abc".isalpha()  # True

# 20. isdigit()
# Only digits
"123".isdigit()  # True

# 21. isalnum()
# Letters + numbers
"abc123".isalnum()  # True

# 22. isspace()
# Only spaces
"   ".isspace()  # True

# 23. islower()
# All lowercase
"abc".islower()  # True

# 24. isupper()
# All uppercase
"ABC".isupper()  # True

# 25. istitle()
# Title case check
"Hello World".istitle()  # True

# 26. center()
# Center align
"hi".center(6, "-")  # '--hi--'

# 27. ljust()
# Left align
"hi".ljust(5, "-")  # 'hi---'

# 28. rjust()
# Right align
"hi".rjust(5, "-")  # '---hi'

# 29. zfill()
# Pad with zeros
"5".zfill(3)  # '005'

# 30. partition()
# Split into 3 parts
"a-b-c".partition("-")  # ('a', '-', 'b-c')

# 31. rpartition()
# Split from right
"a-b-c".rpartition("-")  # ('a-b', '-', 'c')

# 32. format()
# Format string
"Hello {}".format("Pooja")  # 'Hello Pooja'

# 33. encode()
# Convert to bytes
"hi".encode()  # b'hi'

# 34. expandtabs()
# Replace tab with spaces
"a\tb".expandtabs(4)

# 35. casefold()
# Strong lowercase (for comparisons)
"HELLO".casefold()  # 'hello'

# 36. removeprefix()
# Remove prefix
"unhappy".removeprefix("un")  # 'happy'

# 37. removesuffix()
# Remove suffix
"file.txt".removesuffix(".txt")  # 'file'

# 38. isascii()
# Check ASCII characters
"abc".isascii()  # True

# 39. isdecimal()
# Decimal numbers only
"123".isdecimal()  # True

# 40. isnumeric()
# Numeric (more than digits)
"123".isnumeric()  # True

# 41. translate()
# Replace using mapping
table = str.maketrans("a", "x")
"apple".translate(table)  # 'xpple'

# 42. maketrans()
  # Create translation table
str.maketrans("abc", "xyz") # "abc":"xyz"
