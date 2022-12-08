#total chars,lines,words in file
file = open('File_name.txt')
lines = 0
words = 0
chars = 0
for line in file:
    lines += 1
    words += len(line.split())
    chars += len(line.strip('\n'))
print("Lines:", lines)
print("Words:", words)
print("Characters:", chars)
#freq of each char
d = dict()
for c in file:
    if c in d:
        d[c] = d[c] + 1
    else:
        d[c] = 1
print(d)
#rev words
f1 = open("output1.txt", "w")
with open("file.txt", "r") as myfile:
    data = myfile.read()
data_1 = data[::-1]
f1.write(data_1) 
f1.close()
#copy even lines and odd lines of file
fn = open('bcd.txt', 'r')
fn1 = open('nfile.txt', 'w')
cont = fn.readlines()
type(cont)
for i in range(0, len(cont)):
	if(i % 2 ! = 0):
		fn1.write(cont[i])
	else:
		pass
fn1.close()
fn1 = open('nfile.txt', 'r')
cont1 = fn1.read()
print(cont1)
fn.close()
fn1.close()

