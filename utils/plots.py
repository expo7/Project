from matplotlib import pyplot as plt
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
def plot(df):
    fig, ax = plt.subplots(1, figsize=(8, 6))
    fig.suptitle('TRADEING', fontsize=15)
    x=df.index
    ## BB
    # ax.plot(x,df.upper, color="red", label="upper")
    # ax.plot(x,df.lower, color="blue", label="lower")
    ##EMA crossover# ax.scatter(x,df.C*df.EMAsellSig, facecolor='red')
    # ax.scatter(x,df.C*df.EMAbuySig, facecolor='green')
    # ax.plot(x,df.upper, color="red", label="upperBB")
    # ax.plot(x,df.lower, color="blue", label='lowerBB')
    ax.plot(x,df.C,color="black", label='close')

    # ax.plot(x,df.C, color="black", label="close")
    # ax.plot(x,df['macd'],color="blue", label='macd')
    # ax.plot(x,df['sig'],color="brown", label='signal')
    # ax.plot(x,df.EMA30,color='grey',label="30")
    # ax.plot(x,df.EMA20,color='pink',label="20")
    # ax.plot(x,df.EMA10,color='yellow',label="10")
    # ax.scatter(x,df.C*df.EMAbuySig, facecolor='green')
    # ax.scatter(x,df.C*df.BBbuySig, facecolor='green',label='buy')
    # ax.scatter(x,df.C*df.BBsellSig, facecolor='red',label='sell')
    # ax.scatter(x,df.C*df.macdBuy, facecolor='green')
    ax.scatter(x,df.C*df.BUY, facecolor='green')
    ax.scatter(x,df.C*df.SELL, facecolor='red')
    # ax.scatter(x,df.C*df.emaUptrend, facecolor='green')
    # ax.scatter(x,df.C*df.emaDowntrend, facecolor='red')

    # ax.plot(x,df.C,color='black')
    # ax.scatter(x,df.C*df.rsiOversold, facecolor='green')
    # ax.scatter(x,df.C*df.rsiOverbought, facecolor='red')
    plt.ylim([45000, 60000])
    plt.legend(loc="lower right", title="Legend Title", frameon=False)
    plt.show()
