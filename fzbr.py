import hashlib

def main():
	resolverhash = str(input("Ingrese el Hash a resolver: "))
	resolvedor = open("resolvedordeclaves.txt",'r')

	for x in resolvedor.readlines():
		a = x.strip("\n")
		a = hashlib.sha384(a.encode('utf-8')).hexdigest()
		if a == resolverhash:
			print("Clave:  {}      El hash resuelto:   {}".format(x,a))

if __name__ == '__main__':
	main()