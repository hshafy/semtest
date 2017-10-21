"""Main"""

import csv
import sys

def read_csv(filename):
  """
  Read CSV data and return a list with reocrds
  """
  # TODO: get filename from script argument and check path and validate
  data = []
  with open(filename, newline='') as f:
      reader = csv.DictReader(f)
      try:
          for row in reader:
              data.append(process_one_record(row))
      except csv.Error as e:
          sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))
  return data

def process_one_record(record):
  """
  Process each record to update data in one take while reading
  """
  # TODO: check safety of this conversion
  cost = float(record['Cost'])
  if cost != 0:
    record['ROI'] = (float(record['Revenue']) - cost) / cost
  else:
    record['ROI'] = float(record['Revenue'])
  return record


def filter_by_key_value(data, key, value):
  """
  Filter data by key value
  """
  return list(filter(lambda d: d[key] == value, data))

def print_top_kewyord_by_ROI(data, company_name, limit):
  print('')
  filtered_data = filter_by_key_value(data, 'Company', company_name)
  if filtered_data is not None:
    print ('Found {} {} records.'.format(len(filtered_data), company_name))
  else:
    print('No data found for {}.'.format(company_name))

  sorted_by_ROI = sorted(filtered_data, key= lambda k: k["ROI"], reverse=True)
  print('Top {} keywords by ROI for {}'.format(limit, company_name))
  top_10 = sorted_by_ROI[0:limit-1]
  for item in top_10:
    print('Keyword: {0}, ROI: {1:.2f}'.format(item['Search keyword'], item['ROI']))

def main():
  if len(sys.argv) < 2:
    print('Please provide filename as a first argument')
    return

  provided_filename = sys.argv[1]
  data = read_csv(provided_filename)
  if not data:
    print ('No data found')
    return

  print ('Found {} records.'.format(len(data)))

  print_top_kewyord_by_ROI(data, 'GetYourGuide', 10)

  # TODO: get list or remanining company names from data
  print_top_kewyord_by_ROI(data, 'Company A', 10)
  print_top_kewyord_by_ROI(data, 'Company B', 10)
  print_top_kewyord_by_ROI(data, 'Company C', 10)
  print_top_kewyord_by_ROI(data, 'Company D', 10)
  print_top_kewyord_by_ROI(data, 'Company E', 10)

if __name__ == '__main__':
  main()