from collections import defaultdict
def groupAnagrams(strs):
    #First we create a hash map with the keys beeing lists
    anagram_map = defaultdict(list)
    #Create an list to append the groups
    result = []

    #For each word in the list 
    for s in strs:
        #We sort the word in alphabetical order, function sorted() will return a list with the characters of the word in order
        sorted_s = tuple(sorted(s))
        #Make the sorted word a key of our hashmap, than we append the word into the key. With this we group the words in keys of the same letters
        anagram_map[sorted_s].append(s)    
    #For each value in the hashmap, the value is a list of the words in the same key
    for value in anagram_map.values():
        #append the list of words with the same keys
        result.append(value)

    return result

result = groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(result)
#The first group have the letters a,e,t
#The second a,n,t
#The third a,b,t