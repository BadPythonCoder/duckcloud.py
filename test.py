# yes i know tests/* are unit tests, screw off

try:
	from tests.test import test
	import duckcloud
	test(duckcloud) # cursed code i know
except Exception as e:
	print(f"{type(e)}: {str(e)}")
input("press enter to exit...")