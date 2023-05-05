import time
f = open("token.txt")
id, secret = f.read().split(",")
f.close()

def test(dc):
	session = dc.login("cookie.txt", id, secret)
	VMS = session.listVMS()
	vm = next(VMS)
	vm.toggle()
	print(vm.status)