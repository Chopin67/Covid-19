import matchmaker2

me = ['coding', 'homework', 'money', 'reciting poetry']

k = ['homework']
m = ['coding', 'homework', 'sleep']
d = ['money', 'cruises', 'reciting poetry', 'gardening']

match = matchmaker2.bestmatch(me, [['K.', k], ['M.', m], ['D.', d]])

if match == 'K.':
    them = k
elif match == 'M.':
    them = m
else:
    them = d

print('You should go out with', match)
print('Topics to discuss include', ' and '.join(matchmaker2.agreement(me, them)))
print('Topics to avoid include', ' and '.join(matchmaker2.disagreement(me, them)))

