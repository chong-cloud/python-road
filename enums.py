from enum import Enum, unique

WEEK = Enum("WEEK", ["MON", "TUE"])

print(list(WEEK))
# 自动查重
@unique
class Test_enum(Enum):
    red = 1
    green = 2
    blue = 3

print(list(Test_enum))
print(Test_enum.red.value)