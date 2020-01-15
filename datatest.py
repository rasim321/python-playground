from datetime import datetime

raw_date = "2017-01-11"
date_format = "%Y-%m-%d"

parsed_date = datetime.strptime(raw_date, date_format)

print(parsed_date)