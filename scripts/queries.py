import requests
import xml.etree.ElementTree as ET
import pandas as pd
# from storage import store_queries


class SearchTerms:
    def KeywordQuery(self, userInput):
        query = f'{userInput}'
        searchUrl = f'http://google.com/complete/search?output=toolbar&gl=us&q={query}'
        self.response = requests.get(searchUrl)

        def parseResults(self):
            results = []

            tree = ET.ElementTree(ET.fromstring(self.content))
            root = tree.getroot()

            for suggestion in root.findall('CompleteSuggestion'):
                question = suggestion.find('suggestion').attrib.get('data')
                results.append(question)

            return results

        return parseResults(self.response)


# userInput = input('Enter search query: ')

# extractor = SearchTerms()

# answers = extractor.KeywordQuery(userInput)

# store_queries(userQuery=userInput, answers=answers)

# print('Printing Results: ')
# print('-----------------')
# for result in answers:
#     print(result)


# print('-----------------')
# print("Done")
