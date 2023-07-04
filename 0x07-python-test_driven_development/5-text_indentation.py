#!/usr/bin/python3
"""has a function that prints a text with 2 new lines
    after each of these characters: ., ? and :
"""


def text_indentation(text):
    """prints text with two lines added after ., ? and :
        Args:
            text: string to print
        Raises:
            TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    found = False
    for r in text:
        if found and r == ' ':
            continue
        if r == '.' or r == '?' or r == ':':
            print("{}".format(r))
            print()
            found = True
        else:
            print("{}".format(r), end="")
            found = False
