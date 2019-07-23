# PriceActionChannel-Bitmex-Trading-Bot
Python libraries allowing the user to create his own strategies on different tickers ( $XBT, $ETH $TRX,$ADA...).

## EMA.py
This file allows you to create MA and EMA with a specified length and returns them included in the array that you gave as input : 

Exemple : result=ma(result,5) creates MA5 value for every candle in the result array.

You can access by using result[i]["MA5"]
Using ema(result,5) directly creates both EMA5 and MA5 in the array result 

## Fractal.py
This file identifies Higher Highs, Higher Lows,Lower Highs, Lower Lows on every timeframe.  
This file allows you to identify fractals and returns them included in the array that you gave as input :  

Exemple : result=fractal_simple(result)  

You can also check if one of these fractals happened recently with the following functions :  
nearHigherHigh(result,where)  
nearHigherLow(result,where)  
nearLowerHigh(result,where)  
nearLowerLow(result,where)  
  
with result : array of candles  
where : since when ( 1 unit = 1 candle )   

Exemple : nearHigherHigh(result,5) will check if an higher high happened in the last 5 candles.  
!!In order to use these functions, your previously need to use the function fractal_simple(result)!!  
## PriceActionChannel.py  
This file allows you to create PAC with a specified length of EMA and returns them included in the array that you gave as input :   
Exemple : result=pac(result,5) creates PAC value with an EMA5 for every candle in the result array  
The price action channel is build the following way :   
  
higherChannel is the ema value of the higher value of the candle  
lowerChannel is the ema value of the lower value of the candle  
middleChannel is the ema value of the close value of the candle  
  
It returns : 1 if price closed above PAC  
             -1 if price closed in PAC  
             0 if price closed below PAC  
           
You can also check how long the price have been above, below or in the pack with the following functions : 
abovePAC(result,time)  
belowPAC(result,time)  
inPAC(result,time)  
  
with result : array of candles  
where : since when ( 1 unit = 1 candle )  

Exemple : abovePAC(result,5) will check if the price was above PAC for the last 5 candles.  
!!In order to use these functions, your previously need to use the function pac(result,length)!!  
