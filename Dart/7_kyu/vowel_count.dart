import "dart:core";

int getCount(String str){
  int count = 0;
  for (int i=0; i < str.length; i++){
    if ('aeiou'.contains(str[i])){
      count +=1;
    }
  }
  return count;
}