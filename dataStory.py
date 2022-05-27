import pandas
import random
import statistics
import plotly.express as pe

# female data category
data = pandas.read_csv("data.csv")
df = data["quant_saved"].tolist()

graph = pe.scatter(df)
#graph.show()

mean = statistics.mean(df)
median = statistics.median(df)
mode = statistics.mode(df)
print("Population Mean: " , mean, ", Median: " , median, ", and Mode: ", mode)

#----------------------------sampling of data----------------------------------

# randomly selects integer (random_means) a certain # of times, uses random_means 
# to get data, appends data to meanList, statistics to calculate mean of meanList.
def random_means_100(counter):
    meanList = []
    for i in range(0,counter):
        random_means = random.randint(0,len(df)-1)
        value = df[random_means]
        meanList.append(value)
    mean = statistics.mean(meanList)
    return mean

def means_1000():
    finalMeanList = []
    for i in range(0,1000):
        total_means = random_means_100(100)
        finalMeanList.append(total_means)
    mean = statistics.mean(finalMeanList)
    st_dev = statistics.stdev(finalMeanList)
    print("Mean of Sample", mean)
    print("Standard Dev. of Sample", st_dev)

means_1000()





