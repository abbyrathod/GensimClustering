from gensim.summarization import summarize, keywords
from pprint import pprint
from smart_open import smart_open

text = " ".join((line for line in smart_open('TextToString.txt', encoding='utf-8')))

# Summarize the paragraph
pprint(summarize(text, ratio=200, split=True))
#> ('the PLA Rocket Force national defense science and technology experts panel, '
#>  'according to a report published by the')

# Important keywords from the paragraph
print(keywords(text))
#> force zhang technology experts pla rocket