with open("/usr/sbin/john", 'r') as f:
        pwd = f.read()[:-1]
        for i in range(26):
                crack = []
                for c in pwd:
                        crack.append(chr(((ord(c) -97 + i) % 26) + 97))
                print("".join(crack))
