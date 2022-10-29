def febi(index,):
    if(index < 0):
        print('请输入大于0的数!')
        return
    print(index)
    if index > 0:
        febi(index - 1)

febi(6)