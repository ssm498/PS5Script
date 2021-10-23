import time
import random
from PS5Check import ps5test
count = 0
while True:
	count += 1
	'''answer = input("Do you want to exit Y/N: ")
	if "Y" in answer.upper():
		break''' 
	found = ps5test()
	if found:
		print("Returning Found")
		print("Email Sent. Good Luck.")
		break
	else: 
		print("Not Found... Continuing")
		print(count)
	time.sleep(30)


