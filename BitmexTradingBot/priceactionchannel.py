import ema

def pac(result,longueur):
    
    #pacC
    result=ema.ema(result,longueur,"close")
    #pacL
    result=ema.ema(result,longueur,"low")
    #pacU
    result=ema.ema(result,longueur,"high")
   
    for i in range(0,len(result[0])):
            try:
                if(result[0][i]["close"]>=result[0][i]["EMA"+str(longueur)+"high"]):
                    result[0][i]["pac"]=1
                elif(result[0][i]["close"]<=result[0][i]["EMA"+str(longueur)+"low"]):
                    result[0][i]["pac"]=-1
                else:
                    result[0][i]["pac"]=0
            except KeyError:
                pass
    return result

#abovePac since "time" candles
def abovePac(result,time):  
    b=False  
    for i in range(0,time):
        try:
            if(result[0][i]["pac"]==1):
                b=True
            else:
                return False
        except KeyError:
            pass
#checking if we where in PAC before "time" candles
    if(b==True and result[0][time+1]["pac"]==0):
        b=True
    else:
        b=False

    return b
#if the "time" last candle are below pack
def belowPac(result,time):  
    b=False  
    for i in range(0,time):
        try:
            if(result[0][i]["pac"]==-1):
                b=True
        except KeyError:
            pass

    return b

#if one of the "time" candles is in pac
def inPac(result,time):  
    b=False  
    for i in range(0,time):
        try:
            if(result[0][i]["pac"]==0):
                return True
        except KeyError:
            pass
    return b

def inPacLT(result,time):  
    b=False  
    for i in range(0,time):
        try:
            if(result[0][i]["pac"]==0):
                b=True
            else:
                return False
        except KeyError:
            pass
    return b




   

