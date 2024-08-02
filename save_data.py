import pandas as pd

def save_to_csv(data):
    df = pd.DataFrame(data['data'])
    df.to_csv('flights_data.csv', index=False)
