import 'dart:math';

int findSmallestInt(List<int> arr) {
  return arr.reduce(min);
}