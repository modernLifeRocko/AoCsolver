import sys

def main(file):
    pass

if __name__ == "__main__":
    file = sys.argv[1] if len(sys.argv)>1 else 'sample.txt'
    main(file)
