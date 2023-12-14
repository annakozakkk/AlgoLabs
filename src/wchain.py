def write_result_to_file(result):
    with open('wchain.out.txt', 'w') as output_file:
        output_file.write(str(result))


def read_data_from_file():
    with open('wchain.in.txt', 'r') as input_file:
        lines = input_file.readlines()
        words = [word.strip() for word in lines[1:]]
        return words


def find_longest_chain(words):
    word_chain_lengths = {}
    if not words:
        return None

    for word in words:
        word_chain_lengths[word] = 1
    sorted_words = sorted(words, key=len)

    for word in sorted_words:
        for letters in range(len(word)):
            cutted_word = word[:letters] + word[letters + 1:]
            if cutted_word in word_chain_lengths and word_chain_lengths[cutted_word] + 1 > word_chain_lengths[word]:
                word_chain_lengths[word] = word_chain_lengths[cutted_word] + 1
    write_result_to_file(max(word_chain_lengths.values()))
    return max(word_chain_lengths.values())


words = read_data_from_file()
