Luc = '''\
Si vis amari ama
Si vis amari ama
Si vis amari ama
Si vis amari ama
Si vis amari ama
'''

f = open('Lucl.txt', 'w')
f.write(Luc)
f.close()

f = open('Lucl.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line, end='')

f.close()
