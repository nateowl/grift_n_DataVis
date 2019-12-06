import csv
import matplotlib.pyplot as plt

# total medal trends - sample some years (20 year increments)

# 1924, 1948, 1968, 1984, 2006, 2014
# columns 0 (year) and column 4 (country)
#
g_usa = 0
s_usa = 0
b_usa = 0
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


#output a chart here! a line chart would probably be best

plt.title("United States Medals")
medals = [g_usa, s_usa, b_usa]
label = ["Gold","Silver", "Bronze"]
colors = ["#FFD700", "#C0C0C0", "#CD7F32"]

plt.pie(medals, labels=label, colors=colors, startangle=0, autopct='%.1f%%')
plt.show()
