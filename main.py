import utils

def run():
  data = utils.group_by_city(utils.get_data())

  labels = data.keys()

  values = list(map(lambda i : len(i), data.values()))

  utils.generate_bar_chart(labels, values)

if __name__ == '__main__':
  run()