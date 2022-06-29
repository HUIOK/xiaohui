# for i  in range(1,10):
#    for j in range(1,i+1):
#     print(i,"x",j,"=",i*j,end="  ")
#    print()
# 九九乘法表






# light={"红灯":30,"绿灯":35,"黄灯":3}
# while True:
#     for i in light:
#         for j in range(light[i]):
#             print(i,"倒计时还有",light[i]-j,"秒")



username=input("请输入账号：")
password=input("请输入密码：")
if len(username) >=5 and len(username) <=8:
    if username[0] in "qwertyuiopasdfghjklzxcvbnm":
        if  len(password)>=8 and len(password) <=  12:
            print("注册成功！",{username,password})
        else:
            print("密码必须8-12位！")
    else:
        print("账号首字母必须小写开头！")
else:
    print("账号长度不符合")