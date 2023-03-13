import os
import itertools as it


def gen_scantree(dir):
    for e in os.scandir(dir):
        if e.is_dir():
            yield e
            yield from gen_scantree(e.path)
        else:
            yield e


listing = gen_scantree('../../Intermediate')
listing = sorted(listing, key=lambda e: e.is_dir())

for is_dir, elements in it.groupby(listing, key=lambda e: e.is_dir()):
    print('DIR' if is_dir else 'FILE', len(list(elements)))
