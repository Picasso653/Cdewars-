int squareSum(List numbers) {
  int sum = 0;
  for (int number in numbers){
    sum += (number*number);
  }
  return sum;
}