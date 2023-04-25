List<num> tribonacci(List<num> signature, int n) {
  List<num> x = List.from(signature);
  for (int i = 2; i < n - 1; i++) {
    num y = x[i] + x[i - 1] + x[i - 2];
    x.add(y);
  }
  return n > 3 ? x : signature.sublist(0, n);
}