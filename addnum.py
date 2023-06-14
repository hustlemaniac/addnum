import sys
def main():
    args = sys.argv[1:]
    if len(args) > 0:
        print(sum(int(i) for i in args))
    else:
        sys.exit("NO ARGUMENTS PASSED.")

if __name__ == "__main__":
    main()