#add to scroll
s='''
'--------------------------------------------------------------------------------'
scroll 1 - grey

'--------------------------------------------------------------------------------'
i'm grey. 

'--------------------------------------------------------------------------------'
'''
print('\n'.join(list('|*|'+l+'|*|' for l in s.split('\n'))))
