List<int> fifo(int n, List<int> ref) {
  List<int> queue = List<int>.filled(n, -1);
  int j = 0;
  if (ref.isEmpty) {
    return queue;
  }
  for (int i in ref) {
    if (queue.length >= n) {
      if (!queue.contains(i)) {
        queue[j % n] = i;
        j++;
      }
    } else if (!queue.contains(i)) {
      queue.add(i);
    }
  }
  return queue;
}