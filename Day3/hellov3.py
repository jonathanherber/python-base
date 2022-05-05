#!/usr/bin/env python3

__version__= "0.0.3"
__author__= "Jonathan Herber"
__license__= "Unlicense"

import os
import sys

arguments = {
    "lang" : None,
    "count" : 1,
}

for arg in sys.argv[1:]:
    key,value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid option `{key}`")
        sys.exit()
    arguments[key]=value

current_lang = arguments["lang"]
if current_lang is None:
    #current_lang = os.getenv("LANG")
    if current_lang in os.environ:
        current_lang = os.getenv("LANG")
    else:
        current_lang = input("Choose a language:")
        
current_lang = current_lang[:5]

msg = {
    "en_US":"Hello World! ",
    "pt_BR":"Olá Mundo ",
    "es_SP":"Hola Mundo ",
}
print(msg[current_lang] * int(arguments["count"]))

