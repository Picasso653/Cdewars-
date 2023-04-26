bool comp(List<int> a1, List<int> a2) {
  if (a1 == null || a2 == null) {
    return false;
  } else if (a1.isEmpty && a2.isEmpty) {
    return true;
  } else if (a1.isEmpty || a2.isEmpty || a1.length != a2.length) {
    return false;
  }
  List<int> positive = a1.map((j) => j.abs()).toList();
  List<int> a = List.from(positive)..sort();
  List<int> b = List.from(a2)..sort();
  for (int i = 0; i < a.length; i++) {
    if (a[i] * a[i] != b[i]) {
      return false;
    }
  }
  return true;
}