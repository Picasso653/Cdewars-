String countSheep(numb) {
  if (numb<1){
    return '';
  }
  String count = '';
  for (int i=1; i<=numb; i++){
    count += i.toString() + ' sheep...';
  }
  return count;
}