import re

def strip_mud_colors(text):
    # Remove combined bg+fg codes first
    text = re.sub(r"&=[A-Za-z]{2}", "", text)

    # Remove foreground / background codes
    text = re.sub(r"&[+-][A-Za-z]", "", text)

    # Remove reset
    text = text.replace("&n", "")
    text = text.replace("&N", "")
    
    return text