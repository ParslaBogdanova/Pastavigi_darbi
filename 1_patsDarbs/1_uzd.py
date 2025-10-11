elements_10 = {1: '', 2: 'Hēlijs', 3: 'Litijs',
               4: 'Berilijs', 5: 'Bors', 6: 'Ogļūdeņradis',
               7: 'Slāpeklis', 8: '',
               9: 'Fluors', 10: 'Neons'}

elements_10[1] = 'ūdeņradis'
elements_10[8] = 'skābeklis'


# elements_10.copy() tiek izveidota jauna vārdnīca, kas satur tos pašus datus/atlēgas, bet kā atsevišķs objekta atmiņā;
# \n - jaunā rindā;
# elements_11 = elements_10 Netiek veidota jauna vārdīca, tikai jauns mainīgā nosaukums. Bet uz to pašu datu struktūru atmiņā. Kad pievieno jaunu vārdīcu+atslēgu,...
# ...arī mainīgais elements_10 tiek izmainīts./#
elements_10_copy = elements_10.copy()
elements_10_copy.update({11: 'Nātrijs'})

# kad pievieno jaunu vārdnīcu+atslēgu, bet oriģinālā vārdnīca nemainījās.
print(elements_10)

print('\n')

elements_11 = elements_10
elements_11.update({11: 'Nātrijs'})
print(elements_10)
