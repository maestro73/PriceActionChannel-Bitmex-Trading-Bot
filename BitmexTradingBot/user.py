import bitmex
def getUser():
    apiKey =''
    apiSecret = ''
    client = bitmex.bitmex(test=True,api_key=apiKey,api_secret=apiSecret)
    user=client.User.User_getMargin().result()
    return user


def getWalletBalance():

    user=getUser()
    return user[0]["walletBalance"]/100000000


def getRisk(percentageRisk,leverage):
    
    wallet=getWalletBalance()*(percentageRisk/100)
    return wallet*leverage
    
