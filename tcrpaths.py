import os
fnames = os.listdir('tcr')
di = []
seen = set()
for f in fnames:
    has_all = f.endswith('_all.tcr')
    n = (
        os.path.splitext(f)[0]
        .replace('_all', '')
        .replace('_', '')
        .replace('-', '')
        .lower())
    n = n[:12]
    i = 2
    while n in seen:
        n = n[:11] + str(i)
        i = i + 1
    seen.add(n)
    di.append((f, n + '.tcr'))

di.sort(key=lambda x: x[0])
for f, n in di:
    print('        {"file_path": "tcr/' + f + '", "name": "' + n + '"},')
