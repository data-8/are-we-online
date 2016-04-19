with open ("logintemplate.py", "r") as myfile:
    logintest=myfile.read()

for i in range(100):
	test_user_file = open('login_user_' + str(i) + '_test.py', 'w')

	user_name = 'testuser' + str(i)
	test_user_file.write("test_user = '" + user_name + "'\n")

	test_user_file.write(logintest)
	test_user_file.close()
