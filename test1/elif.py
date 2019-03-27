account = 'dollarkiller'
password = 'dollarkiller'

print('please input account')
user_account = input()

print('please input account')

user_password = input()

if user_account == account and user_password == password:
    print('登录成功')
else:
    print('密码错误或账号不存在')

