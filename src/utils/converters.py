import re

type CamelCaseString = str


def to_snake_case(string: CamelCaseString):
    return re.sub(r"([a-z])([A-Z])", r"\1_\2", string).lower()
