from config import  Model

def main():
	username=input('请输入用户名:\n')
	passwd=input('请输入地址:\n')
	user=Model.User()
	result=user.checkValidate(username,passwd)
	if not result:
		print ("用户验证失败")
	else:
		print ("用户注册成功，欢迎进入XX系统!")

if __name__=='__main__':
	main()