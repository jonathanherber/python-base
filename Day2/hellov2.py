#!/usr/bin/env python3

__version__= "0.0.1"
__author__= "Jonathan Herber"
__license__= "Unlicense"

import os

#if __name__ == "__main__":

current_lang = os.getenv("LANG","en_US")[:5]

msg = {
    "en_US":"Hello World!",
    "pt_BR":"Olá Mundo",
    "es_SP":"Hola Mundo",
}
print(msg[current_lang])

