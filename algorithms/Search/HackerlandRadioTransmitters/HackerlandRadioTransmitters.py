#!/bin/python

# hackerrank.com/challenges/hackerland-radio-transmitters
if __name__ == '__main__':
  num_houses, coverage = map(int, raw_input().strip().split())
  house_pos = map(int,raw_input().strip().split())
  house_pos.sort()

  count = 0
  for i in range(num_houses):
    if i == 0 or house_pos[i] > needed:
      left = house_pos[i]
      needed = house_pos[i] + coverage
      count += 1

    if (house_pos[i] - left <= coverage and
        house_pos[i] + coverage > needed):
      needed = house_pos[i] + coverage

  print count

