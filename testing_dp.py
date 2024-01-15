def subsets(lst):
  res = [[]]
  for l in lst:
    res += [each + [l] for each in res]
  return res

if __name__ == '__main__':
  print(subsets([1, 2, 3, 4, 5]))
