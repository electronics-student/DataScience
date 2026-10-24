class Univariate():
    def QuanQual(dataset): 
        Quan = []
        Qual = []
        for columnName in dataset.columns:
            #print (columnName)
            if(dataset[columnName].dtype=="str"):
                #print("qual")
                Qual.append(columnName)
            else:
                #print("quan")
                Quan.append(columnName)
        return Quan,Qual