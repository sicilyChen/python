def arrayRankTransform(arr):
    s=sorted(list(set(arr)))
    res=[]
    dict={}

    for index,i in enumerate(s):
        dict[i]=index+1
    for i in arr:
        res.append(dict[i])
    return res

def main():
    arr = input("请输入一个列表：")
    print(arrayRankTransform(arr))

main()