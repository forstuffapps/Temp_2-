u=lambda:map(int,input().split())


'''
    Maximum Product Subarray
    TC : O(N)
    SC : O(N)
'''

def max_prdt_subarr():
    l=[*u(),]
    t=l[0]
    cm,cn,z,pm,pn=t,t,t,t,t
    for i in l[1:]:
        cm=max(pm*i,pn*i,i)
        cn=min(pm*i,pn*i,i)
        z=max(cm,z)
        pm,pn=cm,cn
    return z


################################################################################


'''
    Count the no of Triangles in the given level
    SPOJ : Count the Triangles
    TC : O(N+T)
    SC : O(N)
'''

def count_the_triangles():
    t=int(input())
    q=[]
    m=-1
    for _ in range(t):
        q.append(int(input()))
        m=max(m,q[-1])
    s,o,e,t,i=0,0,0,0,1
    l=[1]
    while i<=m:
        t+=i
        s+=t
        if i%2!=0:
            o+=t
            l.append(s+e)
        else:
            e+=t
            l.append(s+o)
        i+=1
    for i in q:
        print(l[i])


################################################################################


'''
    Adding all the no's upto N by its binary
    InfyTQ : Sum of binary and decimal numbers
    TC : No. of bits in the no.
    SC : Binary Representation
    Eg : 1=1,2=11,3=22,4=122,5=223,6=333.....
'''

def add_as_bits(n):
    ' default if n==1 : 1 process from 2'
    s=bin(n)[2:]
    t=0
    m=len(s)
    a=2**(m-2)
    l=[0]*m
    for i in range(m):
        if s[i]=='1':
            n-=2**(m-(i+1))
            l[-m+i]+=t+1+n   #n==int('0b'+s[i+1:],2)
            t+=a
        else:
            l[-m+i]+=t
        a//=2
    print(l)


" Remarks : Can use this - int('0b'+s[i+1:],2)...but check if empty string('')  "
"            is passed it shows error   "


##################################################################################


'''
    Least next no to the rightside of the no
    APT : Notes Phase-2 Day-4
    TC : O(N)
    SC : O(N)
    Test Cases
    n=10
    l=[10,15,12,18,20,16,14,8,25,13]
    a=[8,12,8,16,16,14,8,-1,13,-1] #Answer
'''
def from_start(l,n):
    p=[]
    q=[-1]*n
    for i in range(n):
        #print(i)
        while p!=[] and l[p[-1]]>l[i]:
            q[p[-1]]=l[i]
            p.pop()
        p.append(i)
    return q


def from_end(l,n):
    p=[]
    q=[-1]*n
    for i in range(n-1,-1,-1):
        while p!=[] and l[p[-1]]>l[i]:
            p.pop()
        if p!=[]:
            q[i]=l[p[-1]]
        p.append(i)
    return q


######################################################################################