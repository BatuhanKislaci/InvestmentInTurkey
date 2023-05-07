import pandas as pd
import matplotlib.pyplot as plt
def TurkeyGeneral(importData,exportData):
    imports = importData["Total"]
    exports = exportData["Total"]
    years = importData["Year"]

    oldData = []
    for i in range(0,10):
        oldData.append([imports[i],exports[i]])
    
    

    generalDF = pd.DataFrame(oldData,columns=["Import","Export"],index=years)
    print("In Turkey's economy imports are higher than exports so investing in one of the imported goods will be beneficial.")
    
    generalDF.plot.line()
    plt.show()


