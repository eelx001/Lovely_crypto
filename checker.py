from hashDecrypt import hdec
VAULT = '{"data": "M5YT....9Mk+97", "iv": "6CD2Hm...Cg==", "salt": "TkHQ....xaSC/g="}'
PASSWORD = "Awerawer22"
w = hdec()
obj = w.decrypt(PASSWORD, VAULT)
print(obj)