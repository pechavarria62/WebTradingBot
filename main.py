from api.oanda_api import OandaApi
from infrastructure.instrument_collection import instrumentCollection
from stream_example.streamer import run_streamer

if __name__ == '__main__':
    api = OandaApi()    
    data = api.get_account_instruments()
    [print(x['name']) for x in data]
    # instrumentCollection.LoadInstruments("./data")
    # run_streamer()
    
    