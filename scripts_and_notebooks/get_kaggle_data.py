# Importamos librerías
import pandas as pd



def load_data_comp_train():
    train = pd.read_csv('./data/train.csv')
    client = pd.read_csv('./data/client.csv')
    electricity_prices = pd.read_csv('./data/electricity_prices.csv')
    forecast_weather = pd.read_csv('./data/forecast_weather.csv')
    gas_prices = pd.read_csv('./data/gas_prices.csv')
    historical_weather = pd.read_csv('./data/historical_weather.csv')

    return (train, client, electricity_prices, forecast_weather,
            gas_prices, historical_weather)


def load_data_comp_test():
    test = pd.read_csv('./data/example_test_files/test.csv')
    client_test = pd.read_csv('./data/example_test_files/client.csv')
    electricity_prices_test = pd.read_csv('./data/example_test_files/electricity_prices.csv')
    forecast_weather_test = pd.read_csv('./data/example_test_files/forecast_weather.csv')
    gas_prices_test = pd.read_csv('./data/example_test_files/gas_prices.csv')
    historical_weather_test = pd.read_csv('./data/historical_weather.csv')

    return (test, client_test, electricity_prices_test, forecast_weather_test,
            gas_prices_test, historical_weather_test)


def describe_data(data):

    return

def main():
    train, client, electricity_prices, forecast_weather, gas_prices, historical_weather = load_data_comp_train()
    test, client_test, electricity_prices_test, forecast_weather_test, gas_prices_test, historical_weather_test = load_data_comp_test()
    return


