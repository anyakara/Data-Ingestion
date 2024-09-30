import spacy
import pandas as pd

class ProcessData:
    def __init__(self, data_mod_name):
        self.spacyModel = spacy.load(f'{data_mod_name}')

    def run(self, file_name:str, extension:str) -> None:
        returns = pd.read_csv('f{file_name}.{extension}') # even after refactoring
        # maintains a dependability on type -- there is no error catching etc.
        
        for data in returns['text']:
            lemmas=[token.lemma_ for token in self.spacyModel(data)]


def main(param:str):
    process = ProcessData() # process data instance
    process.run()

if __name__ == "__main__":
    main()


"""
Decouple Data IO from the rest of ML Ops
"""