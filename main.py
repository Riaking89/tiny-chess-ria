import time,os,json,urllib.request as ur
U=os.environ['MAKEFUN_ENV_URL']
def P(p,b):
 q=ur.Request(U+p,data=json.dumps(b).encode())
 return json.load(ur.urlopen(q))
V=0,100,320,330,500,900,20000
J=-33,-31,-18,-14,14,18,31,33
Y=-17,-15,15,17
X=-16,-1,1,16
G=Y+X
D=[0,0,J,Y,X,Y+X,G]
Q=range(128)
A=[b'<<<<=>>8=;:<<<<@==>A>>@BFFFF<<<<',b'@B><@@<<:88886646442644264426442']
C=abs
E=[[(t[i//8*4+3-C(i%8-3)]-60)*5 for i in range(64)]for t in A]
T=[(V[C(p)]+(E[1][i] if C(p)==6 else E[0][i] if C(p)==1 else 6-C(i%8-3)-C(i//8-3)))*((p>0)*2-1)for p in range(-6,7)for q in range(128)for i in[(q>>1&56|q&7)^56*(p<0)]]
L=[0]*128
L[0]=2;L[7]=1;L[112]=8;L[119]=4;L[4]=3;L[116]=12
b=[0]*128;e=-1;k=[4,116]
H=[];K=[0]*256
N=0;S=0;Z=0;M=25e4;R=0;F=0;I=1e6
def a(s,y):
 p=2*y-1
 for u in(s+15*(1-2*y),s+17*(1-2*y)):
  if not u&0x88 and b[u]==p:return 1
 for D,p in((J,2),(G,6)):
  for d in D:
   u=s+d
   if not u&0x88 and b[u]==(p if y else-p):return 1
 for d in Y+X:
  u=s+d
  while not u&0x88:
   p=b[u]
   if p:
    if(p>0)==y and(C(p)in(5,3+(d in X))):return 1
    break
   u+=d
 return 0
def g(cp):
 m=[]
 for s in Q:
  p=b[s]
  if not p or(p>0)!=w:continue
  z=C(p)
  if z==1:
   d=32*w-16;u=s+d
   if not u&0x88 and not b[u]:
    if(u>>4)==7*w:m+=[s|u<<7|q<<14 for q in(5,4,3,2)]
    elif not cp:
     m.append(s|u<<7)
     if(s>>4)==6-5*w and not b[s+2*d]:m.append(s|(s+2*d)<<7)
   for u in(s+d-1,s+d+1):
    if u&0x88:continue
    y=b[u]
    if(y and(y>0)!=w)or u==e:
     if(u>>4)==7*w:m+=[s|u<<7|q<<14 for q in(5,4,3,2)]
     else:m.append(s|u<<7)
  else:
   for d in D[z]:
    u=s+d
    while not u&0x88:
     y=b[u]
     if y:
      if(y>0)!=w:m.append(s|u<<7)
      break
     if not cp:m.append(s|u<<7)
     if z in(2,6):break
     u+=d
   if z==6 and not cp and s==116-112*w:
    for j,dd in(((1,1),(2,-1))if w else((4,1),(8,-1))):
     if c&j:
      n2=3-(dd>0);ro=3-7*(dd<0)
      if b[s+ro]==4*(2*w-1)and not any(b[s+dd*x]for x in range(1,n2+1))and not any(a(s+i*dd,not w)for i in(0,1,2)):m.append(s|(s+2*dd)<<7)
 return m
def m(v):
 global w,c,e,S
 f=v&127;u=v>>7&127;q=v>>14
 p=b[f];y=b[u];r=q*(2*w-1)or p
 H.append((b[:],w,c,e,k[:],S))
 S+=T[(r+6)<<7|u]-T[(p+6)<<7|f]
 if y:S-=T[(y+6)<<7|u]
 if C(p)==1 and u==e:
  x=u+16-32*w;S-=T[(b[x]+6)<<7|x];b[x]=0
 if not q and C(p)==6 and C(u-f)==2:
  a=u+1-3*(u<f);t=u-1+2*(u<f);S+=T[(b[a]+6)<<7|t]-T[(b[a]+6)<<7|a];b[t]=b[a];b[a]=0
 b[u]=r;b[f]=0
 if not q and C(p)==6:k[not w]=u
 c&=~(L[f]|L[u])
 e=(f+u)//2*(C(p)==1 and C(u-f)==32)or-1
 w^=1
def u():
 global b,w,c,e,k,S
 b,w,c,e,k,S=H.pop()
def o(ms,pl):
 r=[]
 for v in ms:
  u=v>>7&127;y=b[u]
  if not y and u==e:y=1
  s=10000+C(y)*100-C(b[v&127])if y else 0
  if v>>14:s+=9000
  if v==K[pl]:s+=6000
  r.append((-s,v))
 r.sort()
 return[v for _,v in r]
def s(d,al,be,pl):
 global N,F,R,w,c,e
 N+=1
 if N>=M or(N&1023==0 and time.time()>Z):F=1;return 0
 if F:return 0
 ck=a(k[not w],not w)
 if d>2 and not ck and pl:
  w^=1;t=e;e=-1;x=-s(d-3,-be,1-be,pl+1);e=t;w^=1
  if x>=be:return be
 if d<=0 and not ck:
  x=S if w else-S
  if x>=be:return be
  al=max(al,x)
 ms=o(g(d<=0 and not ck),pl)
 bs=-I;bm=0;lg=0
 for j in ms:
  m(j)
  if a(k[w],w):u();continue
  lg=1
  x=-s(d-1,-be,-al,pl+1)
  u()
  if F:return 0
  if x>bs:bs=x;bm=j
  al=max(al,x)
  if al>=be:K[pl]=j;break
 if not lg:
  if d>0 or ck:return-I+pl if ck else 0
  return al
 if pl==0:R=bm
 return bs
def m2(v):
 return '%c%d%c%d'%(97+(v&7),1+(v>>4&7),97+(v>>7&7),1+(v>>11&7))+('nbrq'[(v>>14)-2]if v>>14 else'')
def s2(x):
 return(ord(x[0])-97+(int(x[1])-1)*16)+((ord(x[2])-97+(int(x[3])-1)*16)<<7)|((('nbrq'.find(x[4])+2)if len(x)>4 else 0)<<14)
def p(f):
 global b,w,c,e,k,S
 R=[4,2,3,5,6,3,2,4]
 b=R+[0]*8+[1]*8+[0]*72+[-1]*8+[0]*8+[-x for x in R]+[0]*8
 w=1;c=15;e=-1;k=[4,116];H.clear();S=0
def main():
 global N,F,Z,R
 while 1:
  r=P('/game',{})
  if r['status']=='done':break
  if r['status']!='your_move':continue
  p(0)
  for mv in r['moves']:m(s2(mv))
  N=0;F=0;Z=time.time()+6;v=0
  for d in range(1,65):
   R=0;s(d,-I,I,0)
   if F or not R:break
   v=R
  P('/move',{'game':r['game'],'move':m2(v)if v else'0000'})
main()
