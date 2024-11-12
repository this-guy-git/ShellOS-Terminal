#SHELLOS FOR TERMINAL V1.0
#CREATED BY THIS-GUY-GIT
#CONCEPT FROM CRYPTICSOFT
#SHELLOS IS A TRADEMARK OF CRYPTICSOFT CORP
a = 1
print("loading ShellOS")
print("Welcome to ShellOS")
print("Type help for Help")
while a == 1:
	b = input("~/ShellOS/")
	if b == "help":
		print("neofetch - displays OS Info")
		print("calc - basic calculator")
		print("notes - basic notepad DOES NOT SAVE")
		a = 1
	elif b == "calc":
		print("first num =")
		n = input()
		print("operation? (*/+-)")
		o = input()
		print("second num =")
		nt = input()
		if o == "+":
			print(n, "+", nt, "=", int(n) + int(nt))
		if o == "-":
			print(n, "-", nt, "=", int(n) - int(nt))
		if o == "*":
			print(n, "*", nt, "=", int(n) * int(nt))
		if o == "/":
			print(n, "/", nt, "=", int(n) / int(nt))
	elif b == "neofetch":
		print("ShellOS Terminal Edition v1.0")
		print("Download ShellOS Official Release on GitHub")
	elif b == "notes":
		txt = 0
		print("ONLY 1 LINE WILL SAVE!")
		txt = input("Press Enter to Exit/ ")
		print(txt)
		print("Save?")
		save = input("y/n/ ")
		if save == "y" or "Y" or "YES" or "Yes":
			name = input()
			try:
				with open('shellostxtfile.txt', 'w') as f:
				   			 f.write(txt)
				   			 f.flush()  # Ensure data is written immediately
			except Exception as e:
				print(f"An error occurred: {e}")
	else:
		print("unknown command",   b)
		a = 1
	
