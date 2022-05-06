'''
本程序使用a数组来记录数独的信息，并对可修改的格子进行修改，直到数独填写完成。使用b数组记录数独原始信息，用以判断方格是否可修改
本程序使用定义了三个函数，
一：guess，用于修改单元格数值（每次调用使单元格值加一），
二：check：判断guess的数值是否合法
三：find_next：寻找下一个要修改的单元格
'''

#guess函数使目标单元格数值+1，若guess函数修改的值不能通过check，则循环调用自己，直至该单元格数值合法，或者数值溢出返回错误。
#若guess函数修改后的值通过了check，则调用find_next 函数寻找下个要修改的单元格，对其使用guess函数，直至计算出数独答案返回结果
def guess(i,j):
    global target
    a[i][j] += 1
    if a[i][j]==10:
        a[i][j] = 0
        return
    else:
        if check(i,j):
            next= find_next(i, j)
            next1=next[0]
            next2=next[1]
            if (next1==i) and (next2==j):
                print('bingo,that\'s the answer!',a)
                target=1
                return
            else:
                guess(next1,next2)

        if target:
            return
        guess(i,j)


#check函数通过对行、列、小九宫格的遍历，寻找是否有其他单元格数值重复
def check(i,j):
    counter=0
    for x in range(9):
        if a[i][x]==a[i][j]:
            counter+=1
        if a[x][j]==a[i][j]:
            counter+=1
        idiv =int(i/3)
        jdiv =int(j/3)
    for o in range(3):
        for p in range(3):
            if a[idiv*3+o][jdiv*3+p]==a[i][j]:
                counter+=1
    if counter>3:
        return 0
    else:
        return 1

#find_next函数每次将‘指针’移到下一个单元格，然后对其是否可修改进行判断（b[m][n]==0）,直到找到下一个可修改的单元格返回对应坐标
def find_next(i,j):
    m=i
    n=j+1
    #使用变量m,n计算下一个方格
    if n>8:
        m+=1
        n=0
    if m==9:
        return i,j
    #当n等于9时，数独应该换行了。接下来是对方格是否可修改数据进行验证（只有数独输入时数字是0的方格才可以变更数据）
    while(b[m][n]!=0):
        if m==8 & n==8:
            return i,j
        elif n < 8:
            n+=1
        else:
            m+=1
            n=0
    return m,n

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
target=0
guess(0,0)