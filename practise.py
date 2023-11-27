# for i in range(int(input())):
#     t=[]
#     l=['c','o','d','e','h','f']
#     c,o,d,e,h,f=0,0,0,0,0,0
#     for j in range(int(input())):
#         n=list(input())
#         t=t+n
#     for i in t:
#         if i in l:
#             if i=='c':
#                 c+=1
#             if i=='o':
#                 o+=1
#             if i=='d':
#                 d+=1
#             if i=='e':
#                 e+=1
#             if i=='h':
#                 h+=1
#             if i=='f':
#                 f+=1
#     c=c//2
#     e=e//2
#     ans=min(c,o,d,e,h,f)
#     print(ans)

# for t in range(int(input())):
#     n=int(input())
#     l=list(map(int,input().strip().split()))
#     ans=[]
#     for i in range(n):
#         if l[i]!=l[i+1]:
#             ans.append(i)
#             ans.append(i+1)
#     print(len(set(ans)))
#     print(ans)
#     print(set(ans))       
            
# class animal:
#     def walk(self):
#         print('1')
# class dog(animal):
#     def walk(self):
#         print('2')
# class cat(animal):
#     def walk(self):
#         print('3')
# class human(cat,dog):
#     pass
# obj=human()
# obj.walk()
# dog.walk(obj)

class encap:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def demo(self):
        print(self.a)
        print(self.b)
        print(self.c)

s1=encap(1,'z','$')
s2=encap('^',1,'m')

s2.demo()