import os

os.system("frida-ps -Uai")
f = str(input("Apk Identifier: "))
milez = 'objection -g '+f+' explore -s "android sslpinning disable"'
os.system(milez)
