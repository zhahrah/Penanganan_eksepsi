import sys
def main():
	print("PROGMAN PEMBAGIAN BILANG")


	a = float(input("Masukkan a: "))
	b = float(input("Masukan b:"))

	try:
		hasil = a / b
	except ZeroDivisionerror:
		print("\nERROR: Nilai b tidak boleh nol")
		sys.exit(1)

	print("\na : ", a)
	print("b : ", b)
	print("a / b= ", hasil)

if __name__ == "__main__":
	main()
