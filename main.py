def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(len(file_contents.split()))

if __name__ == "__main__":
    main()
