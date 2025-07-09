import pandas as pd
import numpy as np
import math
from statistics import NormalDist
import matplotlib as mpl
import matplotlib.pyplot as plt

spi = {
    'Arsenal': [83.9],
    'Aston Villa': [79.3],
    'Bournemouth': [59.6],
    'Brentford': [77.1],
    'Brighton': [80.9],
    'Chelsea': [75.8],
    'Crystal Palace': [73.5],
    'Everton': [63.6],
    'Fulham': [68.2],
    'Leeds': [59.0],
    'Leicester': [64.4],
    'Liverpool': [83.9],
    'Man City': [92.3],
    'Man Utd':  [79.1],
    'Newcastle': [83.7],
    'Nottingham Forest': [56.1],
    'Southampton': [56.7],
    'Spurs': [72.1],
    'West Ham': [70.9],
    'Wolves': [59.1]
    }

spi_df = pd.DataFrame.from_dict(spi)

print(spi_df)

data1 = pd.read_excel('E:\Projects\ML_Soccer\epl-2022-UTC.xlsx', sheet_name='Data1')
df = pd.DataFrame(data1)
gameCount = df.shape[0]
print(gameCount)
goalsHome = np.zeros(gameCount)
goalsAway = np.zeros(gameCount)
for i in range(0, gameCount):
    x = df['Score'][i].split()
    goalsHome[i] = x[0]
    goalsAway[i] = x[2]
df['Home Goals'] = goalsHome
df['Away Goals'] = goalsAway

winner = []
loser = []
for i in range(0, gameCount):
    if df['Home Goals'][i] == df['Away Goals'][i]:
        winner.append('TIE')
        loser.append('TIE')
    elif df['Home Goals'][i] > df['Away Goals'][i]:
        winner.append(df['Home'][i])
        loser.append(df['Away'][i])
    else:
        winner.append(df['Away'][i])
        loser.append(df['Home'][i])
df['Winner'] = winner
df['Loser'] = loser

other = []
for i in range(0, gameCount):
    if df['First Goal'][i] == df['Home'][i]:
        other.append(df['Away'][i])
    elif df['First Goal'][i] == df['Away'][i]:
        other.append(df['Home'][i])
    else:
        other.append("NaN")
df['Other'] = other

print(df)

#Test if Scoring First impacts chances of winning
#Determine the team that scored first - did they win versus did they lose.
p0 = 0
expectedResults = 0
gamesWithGoals = gameCount
for i in range(0, gameCount):
    if (df['Score'][i] == '0 - 0'):
        gamesWithGoals -= 1
        continue
    p0 += spi_df[df['First Goal'][i]] / (spi_df[df['First Goal'][i]] + spi_df[df['Other'][i]])
    if df['First Goal'][i] == df['Winner'][i]:
        expectedResults+=1

p0 /= gamesWithGoals
expectedResults /= gamesWithGoals

# Conduct the 1-Sample Z-Test for Proportions
# H0 = p == p0
# Ha = p != p0
# Two tailed test
phat = expectedResults
p0 = p0
n = gamesWithGoals

z = (phat - p0)/math.sqrt(p0 * (1 - p0) /n)
pvalue = 2 * (1 - NormalDist(mu=0,sigma=1).cdf(z))

# Test if Scoring 1st in First half is better than Second half
# H0: p1 == p2
# Ha: p1 > p2

p1 = 0
n1 = 0
p2 = 0
n2 = 0
for i in range(0,gameCount):
    if (df['Score'][i] == '0 - 0'):
        continue
    # First Half
    if df['Time'][i] <= 45:
        n1 += 1
        if df['First Goal'][i] == df['Winner'][i]:
            p1+=1
    elif df['Time'][i] > 45:
        n2 += 1
        if df['First Goal'][i] == df['Winner'][i]:
            p2 += 1

phat1 = p1/n1
phat2 = p2/n2
phatc = (p1+p2)/(n1+n2)
print(phat1)
print(phat2)
z = (phat1 - phat2)/(phatc * (1 - phatc) * (1/n1 + 1/n2))
pvalue = 1 - NormalDist(mu=0,sigma=1).cdf(z)
print(pvalue)