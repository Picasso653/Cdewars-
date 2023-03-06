import 'dart:math';
isSquare(n) { 
  if (n < 0){
    return false;
  }else {
    int k = sqrt(n).toInt();
    return k*k == n;
  }
}
