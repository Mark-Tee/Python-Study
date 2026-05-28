str = "许多"
stl = str.encode('utf-8')
print(stl)
stl2 = stl.decode('utf-8')
print(stl2)
#encode是将字符串转换为字节串，decode是将字节串转换为字符串
#在Python中，字符串是以Unicode编码的，而字节串是以特定编码（如UTF-8）表示的二进制数据。
#使用encode方法可以将字符串转换为字节串，而使用decode方法可以将字节串转换回字符串。
#在这个例子中，字符串"许多"被编码为UTF-8字节串，然后再解码回字符串。
