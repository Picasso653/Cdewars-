int find(List integers) {
  int odd_number = 0;
  int odd_count = 0;
  int even_number = 0;
  int even_count = 0;
  for (int i=0; i < integers.length; i++){
    if (integers[i]%2==0){
      even_count += 1;
      even_number = integers[i];
    }else{
      odd_count +=1;
      odd_number = integers[i];
    }
    if (odd_count == 1 && even_count > 1){
          return odd_number;
        }else if (odd_count > 1 && even_count == 1){
          return even_number;
          }
  }
  return 0;
}