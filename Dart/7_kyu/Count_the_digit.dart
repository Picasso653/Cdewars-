int nbDig(int n, int d) {
  int count = 0;
  for (int i = 0; i <= n; i++) {
    int square = i * i;
    while (square > 0) {
      if (square % 10 == d) {
        count++;
      }
      square ~/= 10;
    }
  }
  if (d == 0){
    return count+1;
  }
  return count;
}