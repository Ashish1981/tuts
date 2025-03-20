import os, tempfile
from itertools import zip_longest

def grouper(n, iterable, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)
n = 10000
with open('/mnt/c/watson&walker/all_pdfs_m/_ModifiedIntelliMagic.txt') as f:
    for i, g in enumerate(grouper(n, f, fillvalue=None)):
        with tempfile.NamedTemporaryFile('w', delete=False) as fout:
            for j, line in enumerate(g, 1): # count number of lines in group
                if line is None:
                    j -= 1 # don't count this line
                    break
                fout.write(line)
        os.rename(fout.name, 'all_pdfs_m/small_file_{0}.txt'.format(i * n + j))