import math
import numpy as np
import matplotlib.pyplot as plt

priceInit = 100
expected_return = 0.05
volatility = 0.2
simLengthYears = 2
tradesYearly = 252
tradeDay = 1/tradesYearly

prices=[]
days = []
allPaths = []
finalPrices = []

price = priceInit

for j in range(10000):
    prices=[priceInit]
    days = [0]
    for i in range(tradesYearly*simLengthYears):
        days.append(i+1)
        z = np.random.normal(0, 1)
        returnVal = (expected_return-0.5*volatility**2)*tradeDay + volatility*z*math.sqrt(tradeDay)
        price = price * math.exp(returnVal)
        prices.append(price)
    finalPrices.append(price)
    allPaths.append(prices)
    price=priceInit
    
#print(prices)
#print(finalPrices)

finalMean = np.mean(finalPrices)
finalMedian = np.median(finalPrices)
finalStDev = np.std(finalPrices)
finalMin = np.min(finalPrices)
finalMax = np.max(finalPrices)

print("After %s years (%s trading days)" % (simLengthYears, simLengthYears*tradesYearly))
print("With an expected return of "+str(expected_return*100)+" %, volatility of "+str(volatility*100)+" %, initial price of $"+str(priceInit))

print("Mean: ",finalMean)
print("Median: ",finalMedian)
print("Standard deviation: ",finalStDev)
print("Minimum: ",finalMin)
print("Maximum: ",finalMax)

plt.figure()

for path in allPaths[:100]:
    plt.plot(days, path)

plt.xlabel("Trading Day")
plt.ylabel("Price")
plt.title("Simulated Stock Price")
plt.savefig("stock_simulation.png")

plt.figure()
plt.hist(finalPrices, bins=50)
plt.xlabel("Final Stock Price")
plt.ylabel("Frequency")
plt.title("Distribution of Simulated Final Prices")
plt.savefig("final_price_distribution.png")

plt.show()