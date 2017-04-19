title = ' MULTIPLICATION TABLES '
line = len(title) * '-'
print('{}\n{}'.format(title, line))
for x in range(1,13):
	for i in range(1,13):
		f = i
		i = i * x
		print('      {} x {} = {}'.format(x,f,i))
	print('')
