# Trie comes from the word "retrieval" and is a different type of tree
# Typically useful for auto completion

# Each Node has 2 things
    # - a dictionary of children/child nodes
    # - flag saying if this is the end of a word.
# To insert a word, we go letter by letter and insert it into the 

# add h to the root node which points to another node with a dictionary. Add next letter to that dictionary that points to another dictionary

class Node:
    def __init__(self):
        self.children = dict{}
        self.is_end = False 

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        current = self.root
        for c in word: 
            if c not in current.children:
                current.children[c] = Node()
            current = current.children[c]

        current.is_end = True            


    def search(self, word):
        current_node = self.root
        for c in word:
            if c not in current_node.children:
                return False
            current_node = current_node.children[c]
        return current_node.is_end


    def delete(self, current_node, word, index):
        if index == len(word): #Base case: we reached the end of the word
            if not current_node.is_end: #if word does not exist in trie, no end marker
                return False
            current_node.is_end = False #mark end of the word as False(removing word)
            return len(current_node.children) == 0 #if node has no children, return true, because we can only delete this node if it does not have other children

        c = word[index] #Get current character we are processing
        node = current_node.children.get(c) # look for child node corresponding to that character.
        if node is None: # if character is not found, word does not exist --> can exit 
            return False;
        delete_current_node = self.delete(node, word, index+1) #recursively call function on next character, returns true if child node can be safely deleted

        if delete_current_node:
            del current_node.children[c]
            return len(current_node.children) == 0 and not current_node.is_end
        return False
    

    def starts_with(self, prefix): # returns all words that starts with prefix

    def list_words(self): #returns all words in dicitionary


    def has_prefix(self, prefix: str) --> bool:
        node = self.root
        for c in prefix: 
            if c not in node.children:
                return False
            node = node.children[c]
        return True

