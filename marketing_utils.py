import math
import pandas as pd

def getDay(day):
    return pd.to_datetime(day).strftime("%d %b (%a)")

def getNoOfLeads(results):
    if math.isnan(results):
        return 0
    else:
        return results

def getCostPerLead(amountSpent, results):
    costPerLead=amountSpent/results
    if math.isnan(costPerLead):
        return 0
    else:
        return costPerLead

def getCTR(results):
    ctr=round(results,2)
    if math.isnan(ctr):
        return str(0)
    else:
        return str(ctr)

def getLinkClick(linkClick):
    linkClick=round(linkClick,2)
    if math.isnan(linkClick):
        return str(0)
    else:
        return str(linkClick)

def getLPViews(lpv):
    lpv=round(lpv,2)
    if math.isnan(lpv):
        return str(0)
    else:
        return str(lpv)

def getMemerPassed(landingPageViews, linkClicks):
    memberPassed=round((landingPageViews/linkClicks)*100,2)
    if math.isnan(memberPassed):
        return str(0)
    else:
        return str(memberPassed)

def getLPConversion(results, landingPageViews):
    lpConversion=round((results/landingPageViews)*100,2)
    if math.isnan(lpConversion):
        return str(0)
    else:
        return str(lpConversion)
