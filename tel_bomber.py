# Writed by Hack Man :) 
# just use for fun :) 

from pyrogram import Client

print("*** For get api_id and api_hash go to https://my.telegram.org/auth ***")
api_id = int(input("api ID: "))
api_hash = str(input("api HASH: "))
x = 0


idd = str(input("Target id: "))
try :
    idd = int(idd)
except:
    idd = str(idd)
msg = str(input("massage : "))

with Client("ac2", api_id, api_hash) as app:
    while True:
        app.send_message("%s" % idd, "%s" % msg)
        x += 1
        print("%s massage has ben send " % x)
