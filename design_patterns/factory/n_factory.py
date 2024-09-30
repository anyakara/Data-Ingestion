"""Module on how to design data processing systems
in a modular way following the Factory Design Pattern.
This is process-driven development...."""

import spacy
import pandas as pd
from sqlalchemy import create_engine
import datetime


class Process:
    def __init__(self, articleLoader, modelName):
        self.articleLoader = articleLoader
        self.spacyModel = spacy.load(modelName)
    
    def run(self, col_name):
        articles = self.articleLoader.get_articles()
        for text in articles[col_name]:
            lemmas = [token.lemma_ for token in self.spacyModel(text)]


class CSVArticleLoader:
    def __init__(self, fp)->None: # fp=file_path
        self.fp = fp
    
    def get_articles(self):
        return pd.read_csv(self.fp)


class SQLArticleLoader:
    def __init__(self, connectionString):
        self.engine = create_engine(connectionString)
    
    def get_articles(self) -> None:
        return pd.read_sql(`SELECT text FROM articles`, conn=self.engine)


def main_csv(param:str=None)->None:
    process=Process(articleLoader=CSVArticleLoader(fp='{param}.csv'))
    process.run()


def main_sql(param:str):
    process=Process(articleLoader=SQLArticleLoader(connectionString=param))
    process.run()


class LoadSQLEngine:
    pass

class LoadCSVEngine:
    pass

def main(param:LoadCSVEngine | LoadSQLEngine):
    main_sql() if param is LoadSQLEngine else main_csv()


if __name__ == "__main__":
    main()
    # what would typer.run(main) -- is in anyways different