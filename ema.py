def ma(dataset,longueur,price="close",verbose=0):
#price must be : low , high , close
    try:
       for i in range(0,len(dataset[0])):
        somme=0
        for j in range(0,longueur):
           if((i+j)<len(dataset[0])):
                somme+=dataset[0][i+j][price]
                dataset[0][i]["MA"+str(longueur)+price]=somme/(longueur)

        #Print close & MA Longueur#
        if(verbose):
            print("Cloture")
            print(dataset[0][i]["price"])
            print("MA sur "+str(longueur)+" periodes")
            print(dataset[0][i]["MA"+str(longueur)+price])
            print("Heure : ")  
            print(dataset[0][i]["timestamp"])
    except:
        print("Error with assigning MA")
    return dataset

def ema(dataset,longueur,price="close",verbose=0):

    try:
        dataset=ma(dataset,longueur,price,verbose)
        #initializing the oldest one to MA
        dataset[0][len(dataset[0])-longueur]["EMA"+str(longueur)+price]=dataset[0][len(dataset[0])-longueur]["MA"+str(longueur)+price]
        multiplier=2/(longueur+1)
        

        for i in range(len(dataset[0])-longueur-1,-1,-1):
            localPrice=dataset[0][i][price]
            emaY=dataset[0][i+1]["EMA"+str(longueur)+price]
            emaT=(localPrice*multiplier)+(emaY*(1-multiplier))

            dataset[0][i]["EMA"+str(longueur)+price]=emaT

    except KeyError:
        pass
    return dataset
   

