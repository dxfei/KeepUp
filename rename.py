#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-------------------------------------------------------------------------------
# File Name:    rename.py
# Author:       dxf
# Email:        18865735646@139.com
# Created:      2021/06/25 15:23
#-------------------------------------------------------------------------------

import os, time, zipfile, shutil

path = r'C:\Users\18865\Desktop\license文件'
os.chdir(path)

zipfile_names = os.listdir(path)
for zipName in zipfile_names:
    licenseZip = zipfile.ZipFile(zipName)
    licenseZip.extractall()
    licenseZip.close()
    os.unlink(zipName)
    print('zipName:',zipName)
subFolderNames = os.listdir(path)

for subFolder in subFolderNames:
    subPath = os.path.join(path,subFolder)
    if os.path.isdir(subPath):
        for item in os.listdir(subPath):
             full_path = os.path.join(subPath, item)
             shutil.move(full_path, path)
        os.rmdir(subPath)




changeTime = time.strftime("%Y%m%d", time.localtime())
file_names = os.listdir(path)
i = 0
j = 0
for name in file_names:
    if name[-8:-4] == "info":
        os.unlink(name)
        i = i + 1
    else:
        index_num1 = name.index('_')
        index_num2 = name.index('.')
        os.renames(os.path.join(path, name), os.path.join(path, name[0:index_num1]+name[index_num2:]))
        logName = changeTime + ' ' + name + ' ' + name[0:index_num1]+name[index_num2:] + '\n'
        logFile = open(r'C:\Users\18865\Desktop\license\license.log','a')
        logFile.write(logName)
        logFile.close()
        j = j + 1
print("本次一共重命名了{1}个文件。".format(1,j))
print("本次一共删除了{1}个文件。".format(1,i))



