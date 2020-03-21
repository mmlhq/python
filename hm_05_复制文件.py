# 1.打开
file_read = open("README")
file_wriet = open("README[复制]","w")

# 2. 读写
text = file_read.read()
file_wriet.write(text)

# 3. 关闭
file_read.close()
file_wriet.close()