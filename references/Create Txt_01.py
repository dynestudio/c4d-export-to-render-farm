import os

pname="nombre de proyecto"
pframes=" Frames"
form=".txt"

filename=pname+pframes+form

f=open(filename,"w")
f.write(pname+pframes)
f.close()
