from api.oanda_api import OandaApi
from infrastructure.instrument_collection import instrumentCollection
from stream_example.streamer import run_streamer
from simulation.ma_cross import run_ma_sim

if __name__ == '__main__':
    api = OandaApi()    
    print(api.fetch_candles("EUR_USD",granularity="D",price="MB"))
    # data = api.get_account_instruments()
    # [print(x['name']) for x in data]
    # instrumentCollection.LoadInstruments("./data")
    # run_streamer()
    # run_ma_sim(curr_list=["EUR","USD","GBP","JPY","AUD","CAD"])
    