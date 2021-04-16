string = input("write your massage :")
#convert massage with big letters to a massage with low letters
string =string.lower()

a_file = open("words_alpha.txt", "r")
#change the words_alpha.txt to a list naming dictionary
dictionary = []
for line in a_file:
  stripped_line = line.strip()
  dictionary.append(stripped_line)

a_file.close()

answer = []
max_l = len(max(dictionary, key=len))
length = len(string) + 1
for j in range(1,length):
    i = j - 1
    flag = 0
    ans = []
    x = 0
    if j > max_l:
        x = j - max_l
    while(i >= x):
        if string[i:j] in dictionary:
            if i > 0 and answer[(i - 1)]:
                    # appending the word to all the possible sentences
                    temp = list((map(lambda x : x + " "+ string[i:j],\
                    answer[(i - 1)])))
                    for elem in temp:
                        ans.append(elem)
                    flag = 2
            else:
                flag = 1
                answer.append([string[i:j]])
        i=i-1
    # if the substring was not in the dictionary append an empty list to answer
    if flag == 0:
        answer.append([])
    if flag == 2:
        answer.append(ans)
if string in dictionary:
  answer[len(string) - 1].append(string)


print("you mean :", answer[len(string) - 1])