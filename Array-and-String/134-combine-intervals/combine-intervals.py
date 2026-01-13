def combine_intervals(intervals):
  sorted_intervals= sorted(intervals,key= lambda interval: interval[0])
  #print(sorted_intervals)
  combine_intervals=[sorted_intervals[0]]
  for interval in sorted_intervals[1:]:
    current_start,current_end=interval
    last_start,last_end= combine_intervals[-1]
    if last_end>=current_start:
      if current_end>last_end:
        combine_intervals[-1]=(last_start,current_end)
    else:
        combine_intervals.append(interval)
  return combine_intervals

intervals = [
  (1, 4),
  (12, 15),
  (3, 7),
  (8, 13),
]
combine_intervals(intervals)