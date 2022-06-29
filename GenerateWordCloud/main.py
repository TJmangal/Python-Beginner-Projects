
import wordcloud


def read_text_file(file_path):

    with open(file_path) as file:
        text = file.read()
    return text


def calculate_frequencies(text, uninteresting_words_list, punctuations_list):

    word_frequencies = {}

    for letter in text:
        if letter in punctuations_list:
            text = text.replace(letter, "")

    words = text.split()

    for word in words:
        if word not in uninteresting_words_list:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 0
            word_frequencies[word] += 1

    return word_frequencies


if __name__ == "__main__":

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my",
                           "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                           "they", "them", "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was",
                           "were", "be", "been", "being", "have", "has", "had", "do", "does", "did", "but", "at", "by",
                           "with", "from", "here", "when", "where", "how", "all", "any", "both", "each", "few", "more",
                           "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

    content = read_text_file("MyText.txt")
    frequencies = calculate_frequencies(content, uninteresting_words, punctuations)

    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies)
    cloud.to_file("myfile.jpg")

# Need to see how the text can be converted to image in python
