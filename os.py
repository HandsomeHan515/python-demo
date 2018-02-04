import os

print(os.getcwd())

# os.chdir('/Users')

print(os.curdir)

print(os.pardir)

# os.makedirs('han//han//han') # 按照递归方式生成

# os.removedirs('han//han')  # 全部删除

# os.mkdir('han')
# os.mkdir('han/sss')

# os.rmdir('han/sss')  # 只删除sss

# print(os.listdir(r'/Users/handsomehan/Python/demo'))

# os.remove('han.py')  # 删除文件

stat = os.stat('demo1.py')
st_size = stat.st_size  # 文件大小

print(stat, st_size)

print(os.sep)  # Linux下“/”, Windows下“\”

# s = os.sep

# print(os.listdir('%sUsers%shandsomehan%sPython%sdemo' % (s, s, s, s)))

# print(os.linesep)

# print(os.pathsep)

# print(os.system('ls'))  # 执行shell命令

# print(os.environ)

# print(os.path.abspath('demo1.py'))

# print(os.path.split('/Users/handsomehan/Python/demo/demo1.py'))  # 分割成文件路径和文件名

print(os.path.dirname(os.path.abspath('__file__')))  # 当前文件的文件路径

python = os.path.dirname(os.path.dirname(os.path.abspath('__file__')))

