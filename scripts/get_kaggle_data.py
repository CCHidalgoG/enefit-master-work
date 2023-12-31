# Importamos librerías
import vaex as vx



def load_data_comp_train():
    train = vx.read_csv('./data/train.csv')
    client = vx.read_csv('./data/client.csv')
    electricity_prices = vx.read_csv('./data/electricity_prices.csv')
    forecast_weather = vx.read_csv('./data/forecast_weather.csv')
    gas_prices = vx.read_csv('./data/gas_prices.csv')
    historical_weather = vx.read_csv('./data/historical_weather.csv')

    return (train, client, electricity_prices, forecast_weather,
            gas_prices, historical_weather)


def main():
    train, client, electricity_prices, forecast_weather, gas_prices, historical_weather = load_data_comp_train()

