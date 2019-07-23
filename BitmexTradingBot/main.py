import bitmex
import fractal
import ema
import strategy
import priceactionchannel
apiKey =''
apiSecret = ''

client = bitmex.bitmex(test=True,api_key=apiKey,api_secret=apiSecret)

tickerXBT="XBT"
tickerETH="ETH"
tickerEOS="EOSU19"
tickerADA="ADAU19"
tickerBCH="BCHU19"
tickerLTC="LTCU19"
tickerXRP="XRPU19"
tickerTRX="TRXU19"
#getting data
result = client.Trade.Trade_getBucketed(symbol="XBTUSD",binSize="5m",partial=True,count=70,reverse=True).result()
resultEth=client.Trade.Trade_getBucketed(symbol="ETHUSD",binSize="1h",partial=True,count=70,reverse=True).result()
resultEOS=client.Trade.Trade_getBucketed(symbol="EOSU19",binSize="1h",partial=True,count=70,reverse=True).result()
resultADA=client.Trade.Trade_getBucketed(symbol="ADAU19",binSize="1h",partial=True,count=70,reverse=True).result()
resultBCH=client.Trade.Trade_getBucketed(symbol="BCHU19",binSize="1h",partial=True,count=70,reverse=True).result()
resultLTC=client.Trade.Trade_getBucketed(symbol="LTCU19",binSize="1h",partial=True,count=70,reverse=True).result()
resultXRP=client.Trade.Trade_getBucketed(symbol="XRPU19",binSize="1h",partial=True,count=70,reverse=True).result()
resultTRX=client.Trade.Trade_getBucketed(symbol="TRXU19",binSize="1h",partial=True,count=70,reverse=True).result()
#on stock le prix du BTC
prixBTC=result[0][0]["close"]

resultEth=fractal.fractal_simple(resultEth)
resultEth=priceactionchannel.pac(resultEth,36)
resultEth=strategy.extremumsMomentum(resultEth,"1h",client,tickerETH,prixBTC)
result=fractal.fractal_simple(result)
result=priceactionchannel.pac(result,36)
result=strategy.extremumsMomentum(result,"5m",client,tickerXBT,prixBTC)

resultEOS=fractal.fractal_simple(resultEOS)
resultEOS=priceactionchannel.pac(resultEOS,36)
resultEOS=strategy.extremumsMomentum(resultEOS,"1h",client,tickerEOS,prixBTC)

resultADA=fractal.fractal_simple(resultADA)
resultADA=priceactionchannel.pac(resultADA,36)
resultADA=strategy.extremumsMomentum(resultADA,"1h",client,tickerADA,prixBTC)

resultXRP=fractal.fractal_simple(resultXRP)
resultXRP=priceactionchannel.pac(resultXRP,36)
resultXRP=strategy.extremumsMomentum(resultXRP,"1h",client,tickerXRP,prixBTC)

resultTRX=fractal.fractal_simple(resultTRX)
resultTRX=priceactionchannel.pac(resultTRX,36)
resultTRX=strategy.extremumsMomentum(resultTRX,"1h",client,tickerTRX,prixBTC)


