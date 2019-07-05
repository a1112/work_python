import zipfile
import bz2
# 加载压缩文件，创建ZipFile对象
# class zipfile.ZipFile(file[, mode[, compression[, allowZip64]]])
# 参数file表示文件的路径或类文件对象(file-like object)
# 参数mode指示打开zip文件的模式，默认值为'r'，表示读已经存在的zip文件，也可以为'w'或'a'，
# 'w'表示新建一个zip文档或覆盖一个已经存在的zip文档，'a'表示将数据附加到一个现存的zip文档中
# 参数compression表示在写zip文档时使用的压缩方法，它的值可以是zipfile. ZIP_STORED 或zipfile. ZIP_DEFLATED。
# 如果要操作的zip文件大小超过2G，应该将allowZip64设置为True。
'''file_dir = 'base_library.zip'
zipFile = zipfile.ZipFile(file_dir)'''

# 01 ZipFile.infolist() 获取zip文档内所有文件的信息，返回一个zipfile.ZipInfo的列表
'''print(zipFile.infolist())'''
# 02 ZipFile.namelist() 获取zip文档内所有文件的名称列表
'''print(zipFile.namelist())'''
# 03 ZipFile.printdir() 将zip文档内的信息打印到控制台上
'''print(zipFile.printdir())'''


'''
import zipfile
import os
zipFile = zipfile.ZipFile(file_dir)
for file in zipFile.namelist():
    zipFile.extract(file, 'd:/Work')
zipFile.close()
'''
'''ZipFile.extractall([path[, members[, pwd]]])
解压zip文档中的所有文件到当前目录。参数members的默认值为zip文档内的所有文件名称列表，也可以自己设置，选择要解压的文件名称。'''



'''
import tarfile

# 压缩
tar = tarfile.open('your.tar', 'w')
tar.add('/Users/wupeiqi/PycharmProjects/bbs2.log', arcname='bbs2.log')
tar.add('/Users/wupeiqi/PycharmProjects/cmdb.log', arcname='cmdb.log')
tar.close()

# 解压
tar = tarfile.open('your.tar', 'r')
tar.extractall()  # 可设置解压地址
tar.close()
'''
data = b"""\
... Donec rhoncus quis sapien sit amet molestie. Fusce scelerisque vel augue
... nec ullamcorper. Nam rutrum pretium placerat. Aliquam vel tristique lorem,
... sit amet cursus ante. In interdum laoreet mi, sit amet ultrices purus
... pulvinar a. Nam gravida euismod magna, non varius justo tincidunt feugiat.
... Aliquam pharetra lacus non risus vehicula rutrum. Maecenas aliquam leo
... felis. Pellentesque semper nunc sit amet nibh ullamcorper, ac elementum
 dolor luctus. Curabitur lacinia mi ornare consectetur vestibulum."""

with bz2.open("myfile.bz2", "wb") as f:
    unused = f.write(data)