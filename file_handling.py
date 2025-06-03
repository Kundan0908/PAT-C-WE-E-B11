# file handling is used to perform operations on a text file.
# Reading, writing, manipulating file data

# file_ = open(file='../Python_Session-3/dummy.txt',mode='w')
# file_.write('This is my first text file data')
# file_.close()

file_ = open(file='../Python_Session-3/dummy.txt',mode='r')
# print(file_.readlines())
print(file_.readline(10))
