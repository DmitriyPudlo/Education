from xml.etree import ElementTree
tree = ElementTree.parse('newsafr.xml')
root_newsafr = tree.getroot()


def read_news(root_rss_file):
    news_list = [descript.text for descript in root_rss_file.iter('description')]
    news_str = ' '.join(news_list)
    return news_str.split()


def search_top_word(dict_word):
    sorted_freq = sorted([freq_from_mydict for freq_from_mydict in set(dict_word.values())], reverse=True)
    top_word = []
    for num in sorted_freq:
        for word, freq in dict_word.items():
            if len(word) > 6 and freq == num and len(top_word) != 10:
                top_word.append(word)
    return top_word


mydict = {}
for words in read_news(root_newsafr):
    mydict[words] = mydict.get(words, 0) + 1

top_word = search_top_word(mydict)

print(top_word)
