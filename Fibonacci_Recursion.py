import sys

"""
Fibonacci series:
0,1,1,2,3,5,8..etc
numbers series
1,2,3,4,5,6,7..etc
"""

#P.S. indcies start from zero..
#fibonacci numbers start from first-0,
#second-1, third-1, 4th-2, 5th-3, etc


#recursion

def f(n):

    return n if(n<=1)else f(n-1)+f(n-2);
    
#loop  and cache
def get_cache(f): 
    cache = dict() 
    def wrapper(x): 
        if x not in cache: 
            cache[x] = f(x) 
        return cache[x] 
    return wrapper 

@get_cache
def f2(n):
    a,b = 0,1
    for u in range(1,n):
        a,b = b,a+b
    return a


#Tests
#loop
assert(f2(0)==0) #put zero..ok


#start fibonacci series
assert(f2(1)==0)
assert(f2(2)==1)
assert(f2(3)==1)
assert(f2(4)==2)
assert(f2(5)==3)
assert(f2(6)==5)
assert(f2(7)==8)

#recursion
assert(f(0)==0) #put zero..ok


#start fibonacci series
#assert(f(1)==0)#error
assert(f(2)==1)
#assert(f(3)==1)#error
#assert(f(4)==2)#error
#assert(f(5)==3)#error
#assert(f(6)==5)#error
#assert(f(7)==8)#error

#debuging..
n=7

print("loop")
for u in range(n):
    print(f"[{u+1}]=>{f(u)}")
print("-----ok-------\n\n");

print(f2(n))
print("-----ok-------\n\n");


print("recursion")  
for u in range(n):
    print(f"[{u}]=>{f(u)}")
print("-----wrong-------\n\n");

print(f(n))
print("-----wrong-------\n\n");

print("after - its changed")
print("recursion")
for u in range(n):
    print(f"[{u+1}]=>{f(u)}")
print("-----ok-------\n\n");

print(f(n-1))
print("-----ok-------\n\n");


"""
as you can see with recursion implementation like f(n-1)+f(n-2),
you need change var that put in function..
and etc..
any recursion its very slow if that big numbers
"""
#f(444444) #recursion error

#ok,we can increase recurtion limit
sys.setrecursionlimit(24444)
#f(444444) error, you can play with numbers yourself..





#with loop implementation you can do it in..
#and working with big numbers
print("loop and cache working..")
print("try to get big number..wait..")
fb = f2(444444)
print(f"number length: {len(str(fb))} of digits:")
print(fb)
print("GOT it")
#any questions?