import csv
import matplotlib.pyplot as plt

def get_data():
  data = []

  with open('./data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    for row in reader:
      iterable  = zip(header, row)
      data.append({
        key: value for key, value in iterable
      })

  return data

def group_by_city(data):
  grouped_by_city = {}

  for record in data:
    city = record['Make']
    if city not in grouped_by_city:
      grouped_by_city[city] = []
    
    grouped_by_city[city].append(record)

  return grouped_by_city


def generate_bar_chart(labels,values):
  fig, ax = plt.subplots()
  y_pos = range(len(labels))
  ax.bar(y_pos, values)
  plt.xticks(y_pos, labels=labels, rotation=90)
  plt.show()