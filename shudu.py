'''
使用a数组来记录数独的信息，并对可修改的格子进行修改，直到数独填写完成。使用b数组记录数独原始信息，用以判断方格是否可修改
'''
def guess(i,j):
    m=i
    n=j+1
    #使用变量m,n计算下一个方格
    if n>8:
        m+=1
        n=0
    if m==9:
        m=8
        n=8
    #当n等于9时，数独应该换行了。接下来是对方格是否可修改数据进行验证（只有数独输入时数字是0的方格才可以变更数据）
    while(b[m][n]!=0):
        if (m==8 and n==8):
            m=i
            n=j
        elif n < 8:
            n+=1
        else:
            m+=1
            n=0
    #print('the next blank is a',m,n)
    #这里求出了下一个可修改的方格，（如果后续没有可修改方格，则返回正在修改的这个方格以打破while循环
    print(m,n)
    a[i][j] += 1
    #开始对数据进行修改
    if a[i][j]==10:
        print('it is not a true way',a)
        a[i][j] = 0
        return
    #若修改后的数字是10，说明前面的数字设置不对，这里返回上一层递归（后续重新调用guess）
    elif check(i,j):
    #如果修改后的数字不是10，调用check函数来检查该数字是否和同行、同列、同小方格的其他数字冲突
        if i==m&j==n:
            print('bingo,that\'s the answer!',a)
    #若不冲突，且是最后一个格子，那说明成功计算出了正确答案，直接输出正确答案
        else:
            print('now i try to guess ',m,n)
            guess(m,n)
    #若不冲突，且后面还有格子，那就暂时保留本格子的数据，对下一个格子的数字进行猜测。
    guess(i,j)
    #若由于后续格子返回了递归，说明本格子的数字设置有误，再次调用guess，猜本格数字+1是否可行

def check(i,j):
    counter=0
    for x in range(9):
        if a[i][x]==a[i][j]:
            counter+=1
        if a[x][j]==a[i][j]:
            counter+=1
        idiv=int(i/3)
        jdiv=int(j/3)
    for o in range(3):
        for p in range(3):
            if a[idiv*3+o][jdiv*3+p]==a[i][j]:
                counter+=1
    if counter>3:
        return 0
    else:
        return 1

a=[\
[0,6,1,0,3,0,0,2,0],\
[0,5,0,0,0,8,1,0,7],\
[0,0,0,0,0,7,0,3,4],\
[0,0,9,0,0,6,3,7,8],\
[0,0,3,2,7,9,5,0,0],\
[5,7,0,3,0,0,9,0,2],\
[1,9,0,7,6,0,0,0,0],\
[8,0,2,4,0,0,7,6,0],\
[6,4,0,0,1,0,2,5,0]]
b=a[:]
guess(0,0)
