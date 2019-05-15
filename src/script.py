import itertools

files = ['abstract.tex'] + ['chapter%d.tex' % i for i in [1, 2, 3, 4, 5, 6]]

for f in files:
    z = ''
    with open(f, 'r') as fin:
        s = fin.read().split('$$')
        for i, j in zip(itertools.count(), s):
            if i % 2:
                z += '\\[' + j + '\\]'
            else:
                z += j
    with open(f, 'w') as fout:
        fout.write(z)
