#https://overthewire.org/wargames/krypton/krypton2.html
import string


freq='etarionshdluwmfcgypbkvjxq'
canary='MNOPQRSTUVWXYZABCDEFGHIJKL'
cipher='OMQEMDUEQMEK'
d={c[1]:c[0] for c in zip(string.ascii_uppercase,canary)}
print(''.join(d[c] for c in cipher))
