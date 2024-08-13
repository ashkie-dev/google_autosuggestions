from scripts.queries import *
from scripts.storage import *

# from dotenv import load_dotenv
# from scripts import queries


def main():

    userInput = input('Enter search query: ')

    extractor = SearchTerms()

    answers = extractor.KeywordQuery(userInput)
    store_queries(userQuery=userInput, answers=answers)
    print('Printing Results: ')
    print('-----------------')
    for result in answers:
        print(result)


if __name__ == '__main__':
    import sys
    sys.path.insert(0, '.local/')
    sys.path.insert(0, '.scripts/')
    main()
