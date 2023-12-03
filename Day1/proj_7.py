day = int(input('Enter a day: '))
day_mapping = {
    28: "Month",
    30: "Month",
    29: "Month",
    365: "Year",
    366: "Leap year",
}

final_ans = (day_mapping.get(day, 'Not a valid time stamp'))
if final_ans == 'Not a valid time stamp':
  print(f'{day} days does not make up a valid time stamp')
else:
  print(f'{day} days makes up a {final_ans}')
