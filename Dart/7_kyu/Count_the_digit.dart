int nbDig(int n, int d) {
  var count = 0;
  for (var i = 0; i <= n; i++) {
    count += d.toString().allMatches((i*i).toString()).length;
  }
  return count;
}