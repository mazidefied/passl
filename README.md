# passl
bypass ssl pinning with just 7 lines of python code
This is achieved using objection.

#what to do 
1. pip install frida-tools
2. pip install objection
3. push your frida-server and cert-der.crt from burpsuite to /data/local/tmp
4. run frida-server
5. run passl.py
