import bitmex
import fractal
import ema
import priceactionchannel
import user
from decimal import Decimal



def extremumsMomentum(result,TS,client,ticker,prixBTC):
    positions=client.Position.Position_get().result()    
    HG,HL,LL,LH=0,0,0,0
    buy=False

    #checking if HH , LL , HL , LH
    for i in result[0]:
        try:
            HG=(fractal.nearHigherHigh(result,4))
        except KeyError:
                pass
        try:
            HL=(fractal.nearHigherLow(result,4))
        except KeyError:
            pass
        try:
            LL=(fractal.nearHigherHigh(result,4))
        except KeyError:
            pass
        try:
            LH=(fractal.nearLowerHigh(result,4))
        except KeyError:
            pass



    #pour selectionner le nombre de contrats, on décide que l'ordre ne doit pas nous coûter + 3% du portefeuille
    risk=user.getRisk(6,20)

    if(ticker=="XBT" or ticker=="ETH"):
        nbrContracts=0.012*prixBTC
    else:
        nbrContracts=risk/result[0][0]["close"]
    #foreach different position
    for i in range(0,len(positions[0])):
           #variables for stop loss        
           lastCandle=result[0][0]["close"]
           leverage=positions[0][i]["leverage"]
           entryPrice=positions[0][i]["avgEntryPrice"]
           percentage=1+(0.092/10)
           percentageL=(0.092/10)

            #si la position correspond à un ticker dentree et qu'elle est vide
           if((positions[0][i]["underlying"]==ticker or positions[0][i]["underlying"]+"U19"==ticker) and positions[0][i]["avgEntryPrice"]==0 and positions[0][i]["openOrderBuyQty"]==0): 
                  
                   #setting stopLoss
                   if(ticker=="XBT"):
                     stop=round(Decimal(result[0][0]["close"]*percentageL),0)
                   elif(ticker=="ETH"):
                     stop=round(Decimal(result[0][0]["close"]*percentageL),1)
                   elif(ticker=="BCHU19"):
                     stop=round(Decimal(result[0][0]["close"]*percentageL),4)
                   elif(ticker=="EOSU19"):
                     stop=round(Decimal(result[0][0]["close"]*percentageL),7)
                   else:
                     stop=round(Decimal(result[0][0]["close"]*percentageL),8)
                   stop=0-stop
                   
                   #is this a double bottom? getting the 2 last lows
                   lows=fractal.doubleBottom(result,TS)
                   try:
                        lows[2]+=0
                   except:
                        lows.append(0)
                        lows.append(0) 
            #-----------------------------------------------STRATEGY--------------------------------------------------------------------------------#
            #-----------------------------------------------STRATEGY--------------------------------------------------------------------------------#
            #strategy avec higherlow, au dessus du pac depuis 3 et dans le pac au moins une fois dans les 6 derniers
                   if(HL and priceactionchannel.abovePac(result,3) and priceactionchannel.inPac(result,6)):
                       print("---OPEN--- Ticker : "+ticker+" above pac since time + higher low - ")
                       print(result[0][0]["timestamp"])
                       print("Nombre de contrats : ") 
                       print(nbrContracts)
                       print("Prix d'ouverture : "+str(result[0][0]["close"]))
                       print("Prix de cloture : "+str(result[0][0]["close"]*percentage))

                       if(ticker!="XBT"):
                            client.Order.Order_new(symbol=ticker,pegPriceType='TrailingStopPeg', orderQty=nbrContracts,price=result[0][0]["close"],pegOffsetValue=stop).result()
                       else:
                            client.Order.Order_new(symbol=ticker+"USD",pegPriceType='TrailingStopPeg',orderQty=nbrContracts,price=result[0][0]["close"],pegOffsetValue=stop).result()
                        
                   #print("Everything fine for "+ticker+" - "+str(result[0][0]["timestamp"]))
                   return result
#---------------------------------------------------------------------------------CLOTURE----------------------------------------------------------------------------#
    #pour chaque position que l'on hold  
    for i in range(0,len(positions[0])): 
        lastCandle=result[0][0]["close"]
        leverage=positions[0][i]["leverage"]
        entryPrice=positions[0][i]["avgEntryPrice"]
        percentage=1+(0.150/10)
        percentageL=1-(0.092/10)
        if((positions[0][i]["underlying"]==ticker or positions[0][i]["underlying"]+"U19"==ticker) and positions[0][i]["avgEntryPrice"]!=0):  
            if(lastCandle>(entryPrice*percentage)):
                print("---CLOSE--- Ticker : "+ticker+" target acquired ")
                print(result[0][0]["timestamp"])
                print("Nombre de contrats : ") 
                print(nbrContracts)
                print("Prix d'ouverture : "+str(entryPrice))
                print("Prix de cloture : "+str(lastCandle))
                if(ticker=="XBT" or ticker=="ETH"):
                    client.Order.Order_new(symbol=ticker+"USD",ordType = 'Market',execInst ='Close').result()
                else:
                    client.Order.Order_new(symbol=ticker,ordType = 'Market',execInst ='Close').result()
            #stop loss triggered 
            elif(lastCandle<(entryPrice*percentageL)):
                print("---CLOSE--- Ticker : "+ticker+" stop loss ")
                print(result[0][0]["timestamp"])
                print("Nombre de contrats : ") 
                print(nbrContracts)
                print("Prix d'ouverture : "+str(entryPrice))
                print("Prix de cloture : "+str(lastCandle))   
                if(ticker=="XBT" or ticker=="ETH"):
                    client.Order.Order_new(symbol=ticker+"USD",ordType = 'Market',execInst ='Close').result()
                else:
                    client.Order.Order_new(symbol=ticker,ordType = 'Market',execInst ='Close').result()
         

    #print("Everything fine for "+ticker+" - "+str(result[0][0]["timestamp"]))
    return result


