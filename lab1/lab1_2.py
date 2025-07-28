import random

def generate_file(filename, n):
	with open(filename, 'w') as f:
		for _ in range(n):
			f.write(f"{random.randint(150,200)}\n")

sizes={
	"heights_1000.txt":1000,
	"heights_5000.txt":5000,
	"heights_10000.txt":10000,
	"heights_50000.txt":50000
}

for filename,n in sizes.items():
	generate_file(filename,n)
	print(f"Generated {filename} with {n} heights.")
