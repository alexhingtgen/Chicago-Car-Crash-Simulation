"""
Alex Hingtgen and Zak Zahner
"""


import csv 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


#function creating the total crashes per month bar chart
def getMonthlyCrashesGraph():
    monthCounts = {}
    with open('Traffic_Crashes_-_Crashes.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
    
        for line in csv_reader:
            month = line["CRASH_MONTH"]
            monthCounts[month] = monthCounts.get(month, 0) + 1

    names = list(monthCounts.keys())
    values = list(monthCounts.values())

    plt.bar(range(len(monthCounts)), values, tick_label=names)
    plt.xlabel('Month')
    plt.ylabel('Number of Crashes')
    plt.title('Car Crashes per Month')
    plt.savefig('CrashesPerMonth.png')
    plt.clf()

#function creating injury proportion per total crashes, fatalities per total crashes,
#and fatalities per total crashes with injuries pie charts
def getInjuryPieCharts():
    injuryCounts = {}
    with open('Traffic_Crashes_-_Crashes.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
    
        for line in csv_reader:
            injuryTotal = line["INJURIES_TOTAL"]
            if injuryTotal == '':
                continue
            injuryTotal = int(injuryTotal)
            if injuryTotal > 0:
                injuryTotal = '1+ Injuries'
            else:
                injuryTotal = 'No Injuries Reported'
            injuryCounts[injuryTotal] = injuryCounts.get(injuryTotal, 0) + 1

        y = []
        mylabels = []
        for key in injuryCounts:
            
            y.append(injuryCounts[key])
            mylabels.append(key)
            plt.subplot(3, 1, 1)
        plt.pie(y, labels = mylabels)
    plt.title('Proportion of Crashes Resulting in Injury')


    fatalCounts = {}
    with open('Traffic_Crashes_-_Crashes.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for line in csv_reader:
            fatalTotal = line["INJURIES_FATAL"]
            if fatalTotal == '':
                continue
            fatalTotal = int(fatalTotal)
            if fatalTotal > 0:
                fatalTotal = '1+ Fatalities'
            else :
                fatalTotal = 'No Fatalities Reported'
            fatalCounts[fatalTotal] = fatalCounts.get(fatalTotal, 0) + 1
        
        y2 = []
        mylabels2 = []
        for key in fatalCounts:
            y2.append(fatalCounts[key])
            mylabels2.append(key)
            plt.subplot(3, 1, 2)
        plt.pie(y2, labels = mylabels2)
    plt.title('Proportion of Crashes Causing Fatalities')
    
    injuryTotal =  0
    fatalTotal = 0
    with open('Traffic_Crashes_-_Crashes.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for line in csv_reader:
            fatal = line['INJURIES_FATAL']
            injury = line['INJURIES_TOTAL']
            if injury == '':
                continue
            else:
                fatal = int(fatal)
                injury = int(injury)
                injuryTotal = injuryTotal + injury
                fatalTotal = fatalTotal + fatal
        fatalTotalList = [fatalTotal, injuryTotal]
        labels1 = ["Injuries Resulting in Fatalities", "Injuries Resulting in No Fatalities"]
        plt.subplot(3,1,3)
        plt.pie(fatalTotalList, labels = labels1)
        plt.title("Total Injuries vs Total Fatalities")

        plt.savefig('InjuryPotential.png') 
    plt.clf()


#function creating number of crashes in each speed limit and the cost of damages histogram
def getAverageCostHistogram():
    df = pd.read_csv("Traffic_Crashes_-_Crashes.csv")
    x1 = df.loc[df.DAMAGE=='OVER $1,500', 'POSTED_SPEED_LIMIT']
    x2 = df.loc[df.DAMAGE=='$501 - $1,500', 'POSTED_SPEED_LIMIT']
    x3 = df.loc[df.DAMAGE=='$500 OR LESS', 'POSTED_SPEED_LIMIT']
    kwargs = dict(alpha=1, bins=10)
    plt.figure()
    plt.hist(x1, **kwargs, color='g', label='OVER $1,500')
    plt.hist(x2, **kwargs, color='b', label='$501 - $1,500')
    plt.hist(x3, **kwargs, color='r', label='$500 OR LESS')
    plt.legend()
    plt.xlabel('Speed Limit in MPH')
    plt.ylabel('Number of Crashes')
    plt.xticks(np.arange(0,75,5))
    plt.title('Crash Costs per Speed Limits')
    plt.savefig('AverageCostHist.png')
    plt.clf()

#function creating line chart for total crashes at each hour in dry conditions     
def onDry() :
    data = pd.read_csv("Traffic_Crashes_-_Crashes.csv")
    dry = data[(data.ROADWAY_SURFACE_COND == "DRY")]
    dryplot = dry.groupby(['CRASH_HOUR']).count()
    dryplot.rename(columns={'CRASH_RECORD_ID':'DRY'}, inplace=True)
    dryplot = dryplot["DRY"]
    dryplot.plot.line()
    plt.xlabel('Crash Hour in Military Time')
    plt.ylabel('Number of Crashes')
    plt.xticks(np.arange(0,24,3))
    plt.title('Total Crashes at Each Hour on Dry Roads')
    plt.savefig('DryPlot.png')
    plt.clf()

#function creating line chart for total crashes at each hour in wet conditions
def onWet() :
    data = pd.read_csv("Traffic_Crashes_-_Crashes.csv")
    wet = data[(data.ROADWAY_SURFACE_COND == "WET")]
    wetplot = wet.groupby(['CRASH_HOUR']).count()
    wetplot.rename(columns={'CRASH_RECORD_ID':'WET'}, inplace=True)
    wetplot = wetplot["WET"]
    wetplot.plot.line()
    plt.xlabel('Crash Hour in Military Time')
    plt.ylabel('Number of Crashes')
    plt.xticks(np.arange(0,24,3))
    plt.title('Total Crashes at Each Hour on Wet Roads')
    plt.savefig('WetPlot.png')
    plt.clf()

#function creating line chart for total crashes at each hour in snow or slush conditions    
def onSnoworSlush() :
    data = pd.read_csv("Traffic_Crashes_-_Crashes.csv")
    snoworslush = data[(data.ROADWAY_SURFACE_COND == "SNOW OR SLUSH")]
    snoworslushplot = snoworslush.groupby(['CRASH_HOUR']).count()
    snoworslushplot.rename(columns={'CRASH_RECORD_ID':'Snow or Slush'}, inplace=True)
    snoworslushplot = snoworslushplot["Snow or Slush"]
    snoworslushplot.plot.line()
    plt.xlabel('Crash Hour in Military Time')
    plt.ylabel('Number of Crashes')
    plt.xticks(np.arange(0,24,3))
    plt.title('Total Crashes at Each Hour on Snowy or Slushy Roads')
    plt.savefig('SnoworSlushPlot.png')
    plt.clf()

#function creating line chart for total crashes at each hour in icy conditions
def onIce() :
    data = pd.read_csv("Traffic_Crashes_-_Crashes.csv")
    ice = data[(data.ROADWAY_SURFACE_COND == "ICE")]
    iceplot = ice.groupby(['CRASH_HOUR']).count()
    iceplot.rename(columns={'CRASH_RECORD_ID':'Ice'}, inplace=True)
    iceplot = iceplot["Ice"]
    iceplot.plot.line()
    plt.xlabel('Crash Hour in Military Time')
    plt.ylabel('Number of Crashes')
    plt.xticks(np.arange(0,24,3))
    plt.title('Total Crashes at Each Hour on Icy Roads')
    plt.savefig('IcePlot.png')
    plt.clf()

#function creating line chart for total crashes at each hour in all conditions
def onAll() : 
    data = pd.read_csv("Traffic_Crashes_-_Crashes.csv")
    dry = data[(data.ROADWAY_SURFACE_COND == "DRY")]
    dryplot = dry.groupby(['CRASH_HOUR']).count()
    dryplot.rename(columns={'CRASH_RECORD_ID':'DRY'}, inplace=True)
    dryplot = dryplot["DRY"]

    wet = data[(data.ROADWAY_SURFACE_COND == "WET")]
    wetplot = wet.groupby(['CRASH_HOUR']).count()
    wetplot.rename(columns={'CRASH_RECORD_ID':'WET'}, inplace=True)
    wetplot = wetplot["WET"]

    ice = data[(data.ROADWAY_SURFACE_COND == "ICE")]
    iceplot = ice.groupby(['CRASH_HOUR']).count()
    iceplot.rename(columns={'CRASH_RECORD_ID':'ICE'}, inplace=True)
    iceplot = iceplot["ICE"]

    snowslush = data[(data.ROADWAY_SURFACE_COND == "SNOW OR SLUSH")]
    snowplot = snowslush.groupby(['CRASH_HOUR']).count()
    snowplot.rename(columns={'CRASH_RECORD_ID':'SNOW OR SLUSH'}, inplace=True)
    snowplot = snowplot["SNOW OR SLUSH"]

    allConditionsPlot = pd.concat([dryplot, wetplot, iceplot, snowplot], axis=1)
    allConditionsPlot.plot.line()
    plt.xlabel('Crash Hour in Military Time')
    plt.ylabel('Number of Crashes')
    plt.xticks(np.arange(0,24,3))
    plt.title('Total Crashes at Each Hour in All Conditions')
    plt.savefig('AllConditionsPlot.png')
    plt.clf()   