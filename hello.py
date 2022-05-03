#!/usr/bin/env python3

__version__= "0.0.1"
__author__= "Jonathan Herber"
__license__= "Unlicense"

import os

#if __name__ == "__main__":

current_lang = os.getenv("LANG","en_US")[:5]

msg = "Hello World!!"

if current_lang == "pt_BR":
    msg = "Olá Mundo!"
elif current_lang == "it_IT":
    msg = "Ciao Mondo!"



print(msg)

