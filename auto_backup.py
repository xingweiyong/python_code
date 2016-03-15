#coding:utf-8
import os,sys
import filecmp
import re
import shutil
holderlist=[]

def compareme(dir1,dir2): #递归获取更新项函数
    dircomp=filecmp.dircmp(dir1,dir2) 
    only_in_one=dircomp.left_only #源目录新文件或目录
    diff_in_one=dircomp.diff_files #不匹配文件，源目录文件发生改变
    dirpath=os.path.abspath(dir1) #定义源目录绝对路径
    #将更新文件名或目录追加到holderlist
    [holderlist.append(os.path.abspath(os.path.join(dir1,x))) for x in only_in_one]
    [holderlist.append(os.path.abspath(os.path.join(dir1,x))) for x in diff_in_one]
    if len(dircomp.common_dirs)>0: #判断是否存在相同子目录，此处只判断相同子目录，因不同子目录会存在于 diff_in_one中
        for item in dircomp.commom.dirs: #递归子目录
            compareme(os.path.abs(os.path.join(dir1,item)),\
                      os.path.abspath(os.oath.join(dir2,item)))
    return holderlist

def main():
    if len(sys.argv)>2:
        dir1=sys.argv[1]
        print dir1
        dir2=sys.argv[2]
        print dir2
    else:
        print 'Usage:',sys.argv[0],'datadir backupdir'
        sys.exit()
    source_files=compareme(dir1,dir2)
    dir1=os.path.abspath(dir1)

    if not dir2.endswith('/'): dir2=dir2+'/'
    dir2=os.path.abspath(dir2)
    destination_files=[]
    createdir_bool=False

    for item in source_files:
        destination_dir=re.sub(dir1,dir2,item) #将源目录差异文件路径替换成备份路径
        print destination_dir
        destination_files.append(destination_dir)
        if os.path.isdir(item): #备份目录中创建 不存在的目录
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)
                createdir_bool=True
    if createdir_bool:
        destination_files=[]
        source_files=[]
        source_files=compareme(dir1,dir2)
        for item in source_files:
            destination_dir=re.sub(dir1,dir2,item) #将源目录差异文件路径替换成备份路径
            print destination_dir
            destination_files.append(destination_dir)
    print 'update item:'
    print source_files
    print destination_files
    copy_pair=zip(source_files,destination_files)
    for item in copy_pair:
        if os.path.isfile(item[0]):
            print item[0],item[1]
            shutil.copyfile(item[0],item[1])
if __name__=='__main__':
    main()


