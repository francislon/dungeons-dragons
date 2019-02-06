
import sys
import re

if( len(sys.argv) == 2 ):
    file_name=sys.argv[1]
else:
    print("Usage: %s filename" % sys.argv[0])
    exit(1)

fh=open(file_name, "r")

for line in fh.readlines():
    m=re.findall("SOURCE\s+.+ORGANISM_SCIENTIFIC: (.+);.*", line)
    if(m):
        print(m[0])

fh.close()
