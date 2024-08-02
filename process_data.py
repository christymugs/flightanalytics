import pandas as pd

def process_data(filename):
    df = pd.read_csv(filename)
    # Clean and transform data as needed
    return df