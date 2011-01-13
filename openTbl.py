from struct import unpack,unpack_from
fid = open('lab_1.tbl')
ind = 128
#get the number of rows
header = ''
#for x in range(0,10):
#    header += unpack('c',fid.read(1))[0]
#header = unpack('<10c',fid.read(10))
#print 'the header is',header
fid.seek(ind)
a = unpack('c',fid.read(1))[0]
print 'a is ',a
while a>chr(12):
    ind += 1
    a = unpack('c',fid.read(1))[0]
    print 'a is ',a
ind += 1
a = unpack('c',fid.read(1))[0]
print 'a is ',a
while a>chr(12):
    ind += 1
    a = unpack('c',fid.read(1))[0]
    print 'a is ',a

d_count = 1
fcon =1
ind += 36
while fcon == 1:
    fid.seek(ind)
    marker1 = unpack('B',fid.read(1))[0]
    marker2 = unpack('B',fid.read(1))[0]
    #print marker1,marker2
    if marker1 == 0 and marker2 == 75:
        print 'YES'
        fcon = 0
    else:
        d_count += 1
        ind += 12
print 'd_count is',d_count
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
    #    print chann,units
        labels.append((chann + ',' + units))
        ind += 17
        #start aquiring data entries
        for x in range(0,d_count):
            fid.seek(ind)
            aux = unpack('d',fid.read(8))[0]
            if abs(aux) < 10**-150:
                aux=0
            #print aux
            out.append(aux)
            ind += 12
        out.reverse()
        output.append(out)
        #data = flipud(out)
        ind +=7
    else:
        fcon = 0
out= map(lambda *row: list(row), *output )
print labels
for x in out:
    for y in x:
        print y,'\t',
    print '\n'
