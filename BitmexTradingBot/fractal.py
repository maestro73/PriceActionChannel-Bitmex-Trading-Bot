def fractal_simple(dataset,verbose=0):
#getting the 2 last top and 2 last bottoms and comparing them as lower high , lower low, higher high , higher low    
    
    dataset=fractal_test(dataset)
    stopL,stopH=0,0
    highs,lows=[],[]

    for i in range(0,len(dataset[0])):
        dataset[0][i]["i"]=i
        try:

            if(dataset[0][i]['is_higher']==1):

                dataset[0][i]["i"]=i
                highs.append(dataset[0][i])
        except KeyError:
            pass
        try:            
            if(dataset[0][i]['is_lower']==1):
                dataset[0][i]["i"]=i
                lows.append(dataset[0][i])
        except KeyError:
            pass

    #comparing - is_higher high? is_higher_low? is_lower_low? is_lower_high?
    for i in range(0,len(highs)-1):
        if(highs[i]["high"]>highs[1+i]["high"]):
            dataset[0][highs[i]["i"]]["is_higher_high"]=1
        if(highs[i]["high"]<highs[1+i]["high"]):
            dataset[0][highs[i]["i"]]["is_lower_high"]=1
    for i in range(0,len(lows)-1):

        if(lows[i]["low"]<lows[1+i]["low"]):
            dataset[0][lows[i]["i"]]["is_lower_low"]=1  

        if(lows[i]["low"]>lows[i+1]["low"]):
            dataset[0][lows[i]["i"]]["is_higher_low"]=1
    if(verbose):
        print_localExtremums(dataset)
        
    return dataset


#identifying higher high , higher low, lower high,lower low
def fractal_test(dataset):
    try:     
   #top
            for i in range(0,len(dataset[0])-5):
                if(dataset[0][i+4]["high"]<dataset[0][i+3]["high"] and dataset[0][i+3]["high"]<dataset[0][i+2]["high"] and dataset[0][i+2]["high"]>dataset[0][i+1]["high"] and dataset[0][i+1]["high"]>dataset[0][i]["high"]):
                    dataset[0][i+2]["is_higher"]=1
            #bot
                elif(dataset[0][i+4]["low"]>dataset[0][i+3]["low"] and dataset[0][i+3]["low"]>dataset[0][i+2]["low"]  and dataset[0][i+2]["low"]<dataset[0][i+1]["low"] and dataset[0][i+1]["low"]<dataset[0][i]["low"]):
                    dataset[0][i+2]["is_lower"]=1    
        #top
            for i in range(0,len(dataset[0])-5):
                if(dataset[0][i+4]["high"]<dataset[0][i+2]["high"] and dataset[0][i+3]["high"]<dataset[0][i+2]["high"] and dataset[0][i+2]["high"]>dataset[0][i+1]["high"] and dataset[0][i+2]["high"]>dataset[0][i]["high"]):
                    dataset[0][i+2]["is_higher"]=1
            #bot
                elif(dataset[0][i+4]["low"]>dataset[0][i+2]["low"] and dataset[0][i+3]["low"]>dataset[0][i+2]["low"]  and dataset[0][i+2]["low"]<dataset[0][i+1]["low"] and dataset[0][i+2]["low"]<dataset[0][i]["low"]):
                    dataset[0][i+2]["is_lower"]=1
    except:
        print("Error printing highs")
    return dataset    

#printing recent extremums
def print_localExtremums(dataset):
    for i in range(len(dataset[0])-1,0,-1):
        try:
           # print(dataset[0][i])
            if(dataset[0][i]["is_higher_high"]==1):
                print("Candle : ")
                print(dataset[0][i]["timestamp"])
                print("is_higher_high")
                print("Price close : ")
                print(dataset[0][i]["close"])
        except KeyError:
           pass
        try:
            if(dataset[0][i]["is_higher_low"]==1):
                print("Candle : ")
                print(dataset[0][i]["timestamp"])
                print("is_higher_low")
                print("Price close : ")
                print(dataset[0][i]["close"])
        except KeyError:
            pass
        try:
            if(dataset[0][i]["is_lower_high"]==1):
                print("Candle : ")
                print(dataset[0][i]["timestamp"])
                print("is_lower_high")
                print("Price close : ")
                print(dataset[0][i]["close"])
        except KeyError:
            pass
        try:
            if(dataset[0][i]["is_lower_low"]==1):
                print("Candle : ")
                print(dataset[0][i]["timestamp"])
                print("is_lower_low")
                print("Price close : ")
                print(dataset[0][i]["close"])
        except KeyError:
            pass


#did an higherHigh happened [where] period ago
def nearHigherHigh(result,where):
    
    for i in range(0,where):
        try:
            if(result[0][i]["is_higher_high"]):
                return True
        except KeyError:
            pass

    return False
#did an higherLow happened [where] period ago
def nearHigherLow(result,where):
    
    for i in range(0,where):
        try:
            if(result[0][i]["is_higher_low"]):
                return True
        except KeyError:
            pass

    return False

#did an LowerLow happened [where] period ago
def nearLowerLow(result,where):
    
    for i in range(0,where):
        try:
            if(result[0][i]["is_lower_low"]):
                return True
        except KeyError:
            pass

    return False

#did an LowerHigh happened [where] period ago
def nearLowerHigh(result,where):
    
    for i in range(0,where):
        try:
            if(result[0][i]["is_lower_high"]):
                return True
        except KeyError:
            pass

    return False


#is considered a double top or  double bottom , the two lowest lows that dont overcome the threshold depending of the timespan
#default thresholds are 1.5% for 1h chart and 4.5% for the daily chart
def doubleTop(result,binSize):
    seuil,stop=0,0
    highs=[]
    if(binSize=="1m"):
        seuil=0.00040404
    if(binSize=="5m"):
        seuil=0.001515152
    if(binSize=="1h"):
        seuil=0.01515152
    if(binSize=="1d"):
        seuil=0.0454545

    for i in range(0,len(result[0])):
        try:
            if(stop<2 and result[0][i]["is_higher"]==1):
                highs.append(result[0][i])
                stop+=1
        except KeyError:
            pass


    if(highs[0]["high"]<=highs[1]["high"]):
        if(1-(highs[0]["high"]/highs[1]["high"])<seuil):
            return True
    elif(highs[0]["high"]>=highs[1]["high"]):
        if(1-(highs[1]["high"]/highs[0]["high"])<seuil):
            return True


    return False



def doubleBottom(result,binSize):
    seuil,stop=0,0
    lows=[]

    if(binSize=="1m"):
        seuil=0.00040404
    if(binSize=="5m"):
        seuil=0.001515152
    if(binSize=="1h"):
        seuil=0.01515152
    if(binSize=="1d"):
        seuil=0.0454545
    

    for i in range(0,len(result[0])):
        try:
#if bottom is too old , return false
            if(stop<2 and result[0][i]["is_lower"]==1):
                lows.append(result[0][i])
                if(lows[0]["i"]>=5):
                    lows.append(0)
                    return lows
                stop+=1
        except KeyError:
            pass


    if(lows[0]["low"]<=lows[1]["low"]):
        if(1-(lows[0]["low"]/lows[1]["low"])<seuil):
            lows.append(1)
            lows.append(1)
            return lows
    elif(lows[0]["low"]>=lows[1]["low"]):
        if(1-(lows[1]["low"]/lows[0]["low"])<seuil):
            lows.append(1)
            return lows

    lows.append(0)
    lows.append(0)
    return lows





