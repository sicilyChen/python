#集合1.直接{}
s={'python','hello',90}
print(s,type(s))
#2.使用内置函数set()
s2=set({'python','hello',90})
print(s2,type(s2))
s3=set([1,2,33,33,4])
print(s3,type(s3))

#集合间的关系
s4=set([1,2,3,3,3,1])
s5=set([1,3,4,5,9])
s6=set([1,4,3,5])
#1.集合是否相等
print(s3==s4) #False
print(s3!=s5) #True
#2.集合是否是另一个集合的子集
print(s6.issubset(s5)) #True
print(s5.issubset(s4)) #False
#3.集合是否是另一个集合的超算
print(s5.issuperset(s6)) #True
print(s4.issuperset(s6)) #False
#4.两个集合是否没有交集
print(s4.isdisjoint(s5))
print(s5.isdisjoint(s6))
s7={6,8,9,10}
print(s6.isdisjoint(s7)) #没有交集为True

