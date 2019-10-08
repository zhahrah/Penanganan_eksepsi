def main():
	print("PROGRAM PEMBAGIAN BILANGAN ")
	a = float (input ("masukkan a : "))
	b = float (input (" masukkan b : "))
	try :
		hasil = a / b
	except (ZeroDivisionError,ValueError,KeyboardInterrupt):
		print ("\nERROR: anda telah melakukan"+ " kesalahan")
	else :
		print(" \na :", a)
		print(" b :", b)
		print("a / b = ", hasil)

if __name__ == "__main__":
	main()
