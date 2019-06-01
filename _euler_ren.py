
import os


path = 'D:\\code\\1\\'

files = os.listdir(path)

print(files)


# 1-67

for i in range(1, 68):
    f_in = path + str(i) + '.py'
    f_out = str(i).zfill(3) + '.py'
    print(f_in, f_out)


    #
    os.rename(f_in, f_out)