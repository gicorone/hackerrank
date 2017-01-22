#!/bin/python

# hackerrank.com/challenges/mini-max-sum
if __name__ == '__main__':
  numbers = map(int, raw_input().strip().split())
  numbers.sort()
  print sum(numbers[:4]), sum(numbers[1:])
