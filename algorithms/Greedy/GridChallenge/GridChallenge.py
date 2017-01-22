#!/bin/python

# hackerrank.com/challenges/grid-challenge
if __name__ == '__main__':
  num_tests = int(raw_input())

  for _ in range(num_tests):
    size = int(raw_input())
    matrix = []
    ok = True

    for i in range(size):
      row = list(raw_input().strip())
      matrix.append(sorted(row))
    
    for j in range(size):
      for i in range(size - 1):
        if matrix[i][j] > matrix[i+1][j]:
          ok = False    
          break
      if not ok:
        break

    if ok:
      print "YES"
    else:
      print "NO"

