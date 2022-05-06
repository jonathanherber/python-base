#!/usr/bin/env python3

import smtplib

SERVER = "localhost"
PORT=8025



FROM = "jonathanherber15@gmail.com"
TO = ["destino1@server.com","destino2@server.com"]
SUBJECT = "Email via Python"
TEXT = """\
Este é um email do Python
<b>Ola mundo</b> 
"""

message = f"""\
From: {FROM}
To: {", ".join(TO)}
Subject: {SUBJECT}
Text: {TEXT}
"""

with smtplib.SMTP(host=SERVER, port=PORT) as server:
    server.sendmail(FROM,TO,message.encode("utf-8"))
    
#no terminal, python -m smtpd -c DebuggingServer -n localhost:8025
#MIMEtext para criptografar a mensagem  