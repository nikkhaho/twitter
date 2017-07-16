def get_id(tw):
 b="@"
 c=""
 d=[]
 bol=0
 for j in tw:
    if j==b:
     d.append(c)
     bol=1

     c=""
    if bol==1:
      if j==" " or j==":" or j=="\'":
       bol=0

       continue
      c=c+j
 d.append(c)
 return d


def get_tag(tw):
 b="#"
 c=""
 d=[]
 bol=0
 for j in tw:
    if j==b:
     d.append(c)
     bol=1

     c=""
    if bol==1:
      if j==" ":
       bol=0

       continue
      c=c+j
 d.append(c)
 return d
def get_idd(tw):
 b="@"
 c=""
 d=[]
 bol=0
 for j in tw:
    if j==b:
     d.append(c)
     bol=1

     c=""
    if bol==1:
      if j==" " or j==":" or j=="\'" or j=="\\":
       bol=0

       continue
      c=c+j
 d.append(c)
 return d[1]

