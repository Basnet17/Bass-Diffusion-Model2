'''
Pritam Basnet
firstproject.py
10/06/2017
This project plots the graph of three different cases with regular contagion, no contagion and slow adoption. It also plots the graph of rates of changes.
'''
import matplotlib.pyplot as pyplot
def productDiffusion(chanceAdoption, socialContagion, weeks, dt):
    '''
    This function simulates the product adoption over time in the Market
    Parameters:
        chanceAdooption: it is the chance of product adoption by the non-adopters.
        socialContagion - it measures the interaction between adopters and non-adopters
        weeks: no of weeks
        dt: the small time difference.
    Return Values:
        timeList: The list of time for plotting X-Axis.
        aList: the list with the adoopters
        rList: the list with rate of changes
    '''
    aList = []
    timeList = []
    t = 0
    adoptersBefore = 0
    aList.append(adoptersBefore)
    timeList.append(t)
    rList = [0]
    
    for i in range(0, int(weeks/dt)+1):
        adopters = aList[-1] + chanceAdoption*(1 - aList[-1])*dt + socialContagion * aList[-1] *(1 - aList[-1])*dt     #differential equations for adopters
        aList.append(adopters)
        t = t + dt
        timeList.append(t)
        rate_of_change = (adopters - adoptersBefore) / dt
        rList.append(rate_of_change)
        adoptersBefore = adopters
        
    return timeList,aList,rList                                                 #returns the lists for other places in the program.
def main():
    chanceAdoption = 0.002                                                       #situation 1
    socialContagion =1.03
    weeks = 15
    dt = 0.01
    pyplot.figure(1)
    timeList1, aList1, rList1 = productDiffusion(chanceAdoption, socialContagion, weeks, dt)  # plots the graph with calling the function.
    pyplot.plot(timeList1, aList1, label = 'Regular')
    pyplot.xlabel('Week')
    pyplot.ylabel('Market Adoption Percent')
    pyplot.legend()
    pyplot.figure(2)
    pyplot.plot(timeList1, rList1, label = 'Regular')
    pyplot.xlabel('Week')
    pyplot.ylabel('Marginal Market Adoption Percent')
    pyplot.legend()
    
    chanceAdoption = 0.00001                                                     #situation 2
    socialContagion= 1.03
    pyplot.figure(1)
    timeList2, aList2, rList2 = productDiffusion(chanceAdoption, socialContagion, weeks, dt)
    pyplot.plot(timeList2, aList2, label = 'Slow Adoption')
    pyplot.xlabel('Week')
    pyplot.ylabel('Market Adoption Percent')
    pyplot.legend()
    pyplot.figure(2)
    pyplot.plot(timeList2, rList2, label = 'Slow Adoption')
    pyplot.xlabel('Week')
    pyplot.ylabel('Marginal Market Adoption Percent')
    pyplot.legend()
    
    chanceAdoption = 0.2                                                          #situation 3
    socialContagion = 0
    pyplot.figure(1)
    timeList3, aList3, rList3 = productDiffusion(chanceAdoption, socialContagion, weeks, dt)
    pyplot.plot(timeList3, aList3, label = 'No Contagion')
    pyplot.xlabel('Week')
    pyplot.ylabel('Market Adoption Percent')
    pyplot.legend()
    pyplot.figure(2)
    pyplot.plot(timeList3, rList3, label = 'No Contagion')
    pyplot.xlabel('Week')
    pyplot.ylabel('Marginal Market Adoption Percent')
    pyplot.legend()
    
    
    pyplot.show()
main()
    
    
                   
    
