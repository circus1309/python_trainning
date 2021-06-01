a = 3**20 #次方
print(a)

x = 10
x*=10 #x=x*10
print(x)

q = w = e = 25
print(q,w,e)
z,x,c, = 11, 22, 33
print(z,x,c)
#續行方式1
y = q \
    + w \
    + e \
    + 12
print(y)
#續行方式2
v = ( z #PEP 8 風格
+ x     #此處可加註解
+ c
+ 12 )
print(v)