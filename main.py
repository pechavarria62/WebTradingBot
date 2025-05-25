from api.oanda_api import OandaApi
from infrastructure.instrument_collection import instrumentCollection
from stream_example.streamer import run_streamer
from simulation.ma_cross import run_ma_sim
from dateutil import parser
from infrastructure.collect_data import run_collection

if __name__ == '__main__':
    api = OandaApi()

    instrumentCollection.LoadInstruments("./data")
    run_collection(instrumentCollection,api)

    # dfr = parser.parse("2023-04-01T01:00:00Z")
    # dto = parser.parse("2023-04-28T02:00:00Z")

    # df_candles = api.get_candles_df("EUR_USD", granularity="H1", date_f=dfr, date_t=dto)

    # print(df_candles.head())
    # print()
    # print(df_candles.tail())


    # print(api.fetch_candles("EUR_USD",granularity="D",price="MB"))
    # data = api.get_account_instruments()
    # [print(x['name']) for x in data]
    # instrumentCollection.LoadInstruments("./data")
    # run_streamer()
    # run_ma_sim(curr_list=["EUR","USD","GBP","JPY","AUD","CAD"])
    