import pandas as pd
from llama_index.core.query_engine import PandasQueryEngine

from src.constants import POPULATION_PATH


def extract():
    """Extract data from the source."""
    return pd.read_csv(POPULATION_PATH)


def transform(data):
    """Transform the data."""
    return data


def load(data):
    """Load the data."""
    population_query_engine = PandasQueryEngine(df=data, verbose=True)

    return population_query_engine
