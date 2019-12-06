import csv
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# total medal trends - sample some years (20 year increments)

# 1924, 1948, 1968, 1984, 2006, 2014
# columns 0 (year) and column 4 (country)
#
g_usa = 0
s_usa = 0
b_usa = 0
g_can = 0
s_can = 0
b_can = 0

#remove row 1 because it is
categories = []


#opens up csv file with csv reader
with open('OlympicsWinter.csv') as csvfile:
	reader = csv.reader(csvfile)

	line_count = 0

#removing the first line of code so that it isn't included in our chart.
	for row in reader:
			if line_count == 0:
				#parse the first row of the text data out of the file
				categories.append(row)
				line_count += 1

			else:

				if (row[7] == "Gold") and (row[4] == "USA"):
					g_usa += 1
				elif (row[7] == "Silver") and (row[4] == "USA"):
					s_usa += 1
				elif (row[7] == "Bronze") and (row[4] == "USA"):
					b_usa += 1
				elif (row[7] == "Gold") and (row[4] == "CAN"):
					g_can += 1
				elif (row[7] == "Silver") and (row[4] == "CAN"):
					s_can += 1
				elif (row[7] == "Bronze") and (row[4] == "CAN"):
					b_can += 1


#output a chart here! a line chart would probably be best

labels = ['Gold', 'Silver', 'Bronze']
canada = [g_can, s_can, b_can]
usa = [g_usa, s_usa, b_usa]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, canada, width, label='Canada')
rects2 = ax.bar(x + width/2, usa, width, label='USA')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Medal Count')
ax.set_title('Medals per country')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()
