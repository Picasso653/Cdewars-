List<int> productArray(List<int> nums) {
  List<int> prod = [];
  for (int i = 0; i < nums.length; i++){
    int m = 1;
    for (int j = 0; j < nums.length; j++){
      if (j != i){
        m *= nums[j];
      }
    }
    prod.add(m);
  }
  
  return prod;
}