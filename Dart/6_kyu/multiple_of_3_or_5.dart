int solution(int n) {
  int i = 0;
  int sum = 0;
  while(i < n){
    if((i % 3 == 0) | (i % 5 == 0)){
      sum += i;
    }
    i += 1;
  }
  return sum;
}