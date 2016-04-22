#coding:utf-8
#python tempfile

'''
    import tempfile
    
    如何你的应用程序需要一个临时文件来存储数据，
    但不需要同其他程序共享，那么用TemporaryFile
    函数创建临时文件是最好的选择。其他的应用程序
    是无法找到或打开这个文件的，因为它并没有引用
    文件系统表。用这个函数创建的临时文件，关闭后
    会自动删除。
'''

import os
import tempfile

def make_file():
    '''创建临时文件，不过创建后，需要手动移除
        os.remove(file)
    '''
    file_name = 'c:\\f1\\test.%s.txt' % os.getpid()
    temp = open(file_name, 'w+b')
    try:
        print('temp : {}'.format(temp))
        print('temp.name : {}'.format(temp.name))
        temp.write(b'hello, I\'m Hongten')
        temp.seek(0)
        print('#' * 50)
        print('content : {}'.format(temp.read()))
    finally:
        temp.close()
        #os.remove(file_name)

def make_temp_file():
    '''创建临时文件，在关闭的时候，系统会自动清除文件'''
    temp = tempfile.TemporaryFile()
    try:
        print('temp : {}'.format(temp))
        print('temp.name : {}'.format(temp.name))
        temp.write(b'hello, I\'m Hongten')
        temp.seek(0)
        print('#' * 50)
        print('content : {}'.format(temp.read()))
    finally:
        temp.close()  #then the system will automatically cleans up the file

def main():
    make_file()
    print('#' * 50)
    make_temp_file()
    
if __name__ == '__main__':
    main()
