def longest_len(lst):
    longest = max(lst, key=len)
    return longest


word_list = ["one", "thelongestwordinthelist", "dictionaries", "Samuel", "greetings"]

print(longest_len(word_list))
