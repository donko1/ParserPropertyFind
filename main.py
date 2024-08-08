
import os

def main():
	if not os.path.isdir("cache"):
		os.mkdir("cache")
	if not os.path.isdir("out"):
		os.mkdir("out")

if __name__ == '__main__':
	main()
