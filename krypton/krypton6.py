#https://overthewire.org/wargames/krypton/krypton6.html
#property 1 of LSFR: a seed of length n gives at most 2**n key, oftentimes shorter
#here key length is 30
#property 2 of LSFR: feeding 0 into LSFR gives the key
from krypton.krypton4 import decode_caesar


key='EICTDGYIYZKTHNSIRFXYCPFUEOCKRNEICTDG'
cipher='PNUKLYLWRQKGKBE'
shifts=[ord(k)-ord('A') for k in key]
print(''.join(decode_caesar(c,shift) for c,shift in zip(cipher,shifts)))
