import sys
with open(sys.argv[1], 'r') as f:
    text_in = f.read()

text_in = text_in[text_in.find("START")+5:text_in.find("STOP")-1].split(' ')
text_out = ''
for i in range(len(text_in)):
    if i % 2 == 0:
        text_out += (text_in[i] + ' ')

with open(sys.argv[2], 'w') as f:
    f.write(text_out.strip() + '\n')