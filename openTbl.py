from struct import unpack,unpack_from
fid = open('lab_1.tbl')
ind = 128
fid.seek(ind)
a = unpack('c',fid.read(1))[0]
while a>chr(12):
    ind += 1
    a = unpack('c',fid.read(1))[0]
ind += 1
a = unpack('c',fid.read(1))[0]
while a>chr(12):
    ind += 1
    a = unpack('c',fid.read(1))[0]

d_count = 1
fcon =1
ind += 36
while fcon == 1:
    fid.seek(ind)
    marker1 = unpack('B',fid.read(1))[0]
    marker2 = unpack('B',fid.read(1))[0]
    if marker1 == 0 and marker2 == 75:
        fcon = 0
    else:
        d_count += 1
        ind += 12
ind = 122
data = []
labels = []
fcon = 1;
output = []
while fcon == 1:
    fid.seek(ind)
    marker1 = unpack('B',fid.read(1))[0]
    marker2 = unpack('B',fid.read(1))[0]
    if marker1 == 0 and marker2 == 75:
        out = []
        ind = ind + 6
        fid.seek(ind)
        units = ''
        a = unpack('c',fid.read(1))[0]
        while a > chr(12):
            units += a
            ind += 1
            a = unpack('c',fid.read(1))[0]
        ind += 1
        chann = '';
        a = unpack('c',fid.read(1))[0]
        while a > chr(12):
            chann += a
            ind += 1
            a = unpack('c',fid.read(1))[0]
        labels.append((chann + ',' + units))
        ind += 17
        #start aquiring data entries
        for x in range(0,d_count):
            fid.seek(ind)
            aux = unpack('d',fid.read(8))[0]
            if abs(aux) < 10**-150:
                aux=0
            out.append(aux)
            ind += 12
        out.reverse()
        output.append(out)
        ind +=7
    else:
        fcon = 0
out= map(lambda *row: list(row), *output )

if __name__ == '__main__':
    for label in labels:
        print label,'\t',
    print ''
    for x in out:
        for y in x:
            print y,'\t',
        print '\n',
 
