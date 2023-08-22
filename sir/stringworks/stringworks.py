# word="hello"
# print(word.capitalize()) #to capitalize the first character 
# #casefold() to lowercase the given string 
# print(word.casefold())
# #count(ch) count of the specified character 
# print(word.count("l"))
# #split(separator) to split into a list using the separator
words="hello world"
# print(words.split(" "))
# print(words.find("ello")) #to find the given str location
#startswith() to find the word starts with the given character if yes true else false 
# print(words.startswith("he"))
# # endswith() to find the given string ends with the given charachter 
# print(words.endswith("rld"))
# isalpha() is used to find the given string is alphabetic order if yes return true else false 
# print(words.isalpha()) #space is not a character
# isdigit() to findn the given string is digit or not 
# print(words.isdigit())
# isalnum() used to check the string is number or alphabet 
# alnum="123hello"
# print(alnum.isalnum())





# text="one 100 and fifty 5"
# # #100,5 
# # words=text.split(" ")
# # for i in words:
# #     if i.isdigit():
# #         print(i,end=" ") 

# nums=[i for i in text.split(" ") if i.isdigit()]
# print(nums)


# text="england promised to continue its aggressive aproach to the cricket "
# # words=text.split(" ")
# vowels={"a","e","i","o","u","A","E","I","O","U"}
# # for i in words:
# #     if i[0].casefold() in vowels:
# #         print(i)
# words=[i for i in text.split(" ") if i[0] in vowels]
# print(words)


text="hello i am here in kakkanad"
# print longest word 
words=text.split(" ")
print(max(words,key=lambda w:len(w)))
 

