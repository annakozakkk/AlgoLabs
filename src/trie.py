
class TrieNode:

    def __init__(self):
        self.children = [None] *26

        self.is_end_of_word = False


class Trie:

    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def symbol_to_index(self, char):
        return ord(char) - ord('a')

    def insert(self, key):
        current_node = self.root
        for symbol in key:
            index = self.symbol_to_index(symbol)
            if not current_node.children[index]:
                current_node.children[index] = self.getNode()
            current_node = current_node.children[index]
        current_node.is_end_of_word = True

    def search(self, key):
        current = self.root
        for symbol in key:
            index = self.symbol_to_index(symbol)
            if not current.children[index]:
                return False
            current = current.children[index]

        return current.is_end_of_word

    def find_prefix(self, prefix):
        current_node = self.root
        for symbol in prefix:
            index = self.symbol_to_index(symbol)
            if not current_node.children[index]:
                return False
            current_node = current_node.children[index]
        return True


def build_trie(keys):
    trie = Trie()
    for key in keys:
        trie.insert(key)
    return trie




