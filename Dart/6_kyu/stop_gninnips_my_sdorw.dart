String spinWords(String str) {
  List<String> spin = str.split(' ');
  for(int i=0; i < spin.length; i++){
    if(spin[i].length >= 5){
      spin[i] = spin[i].split('').reversed.join();
    }
  }
  return spin.join(' ');
}