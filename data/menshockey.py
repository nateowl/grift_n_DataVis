import csv 
import matplotlib.pyplot as plt

#pie chart for men's hockey medal colours (gold, silver, bronze)
# arrays for each


golds = []
silver = []
bronze = []

categories = []


#opens up csv file with csv reader
with open('menshockey.csv') as csvfile:
	reader = csv.reader(csvfile)

	line_count = 0

#removing the first line of code so that it isn't included in our chart.
	for row in reader:
			if line_count is 0:
				#parse the first row of the text data out of the file
				categories.append(row)
				line_count += 1 
			else:
				if row[7] == "Gold":
					print("won gold")
					golds.append(row[7])

				elif row[7] == "Silver":
					print("won silver")
					silver.append(row[7])

				elif row[7] == "Bronze":
					print("won bronze")
					bronze.append(row[7])

				line_count += 1

print(len(golds))
print(len(silver))
print(len(bronze))

# a plot pie chart

labels = ("Gold", "Silver", "Bronze")
sizes = [len(golds), len(silver), len(bronze)]
colors = ['gold', 'silver', 'darkgoldenrod']
explode = [0.1, 0.1, 0.1]

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')

plt.legend(labels, loc=1)
plt.title("Medals For Men's Hockey")
plt.xlabel("Medals since 1924")
plt.show()

