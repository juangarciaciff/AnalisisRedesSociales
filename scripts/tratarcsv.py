#!/usr/bin/env python
import csv

rfp = csv.reader(open('../data/03001sc.csv', 'rb'), delimiter=';')

nfp = open('../data/nodos.csv', 'wb')
nfp.write('ID;LABEL\n')

afp = open('../data/aristas.csv', 'wb')
afp.write('SOURCE;TARGET;WEIGHT\n')

for index, row in enumerate(rfp):
    if index == 0:
        id = 0
        for dato in row:
            id = id + 1
            nfp.write(str(id) + ';' + dato + '\n')
            print '- Nodo:', dato
    else:
        id = 0
        for dato in row[1:]:
            id = id + 1
            if int(dato) > 0:
                print '- arista: (%2s)-- %6s -->(%2s)' % (index, dato, id)
                afp.write(str(index) + ';' + str(id) + ';' + dato + '\n')

nfp.close()
afp.close()
