with open("D:\\Python\\Googler\\1 Python fundamentals\\file access\\shakespear.txt", mode="r") as s_file:
    all_words = list()
    for line in s_file.readlines():
        word = line.strip().split(" ")
        all_words += word
        print(word)

        unique_word = set(all_words)
        print(unique_word)

    with open("D:\\Python\\Googler\\1 Python fundamentals\\file access\\Unique_word.txt", mode="w") as write_file:
        for item in sorted(unique_word):
            write_file.write(item)
            write_file.write("\n")

print(all_words)