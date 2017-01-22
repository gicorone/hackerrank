#!/bin/python

# hackerrank.com/challenges/flipping-the-matrix
if __name__ == '__main__':

  num_tests = int(raw_input().strip())
  for _ in range(num_tests):
    size = int(raw_input())

    matrix = []
    for i in range(2 * size):
      matrix.append(map(int, raw_input().split()))

    total = 0
    for i in range(size):
      for j in range(size):
        total += max(matrix[i][j],    matrix[i][-1-j],
                     matrix[-1-i][j], matrix[-1-i][-1-j])

    print total
