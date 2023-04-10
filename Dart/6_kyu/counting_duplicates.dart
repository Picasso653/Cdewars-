int duplicateCount(String text){
  var uniqueChars = text.toLowerCase().split('').toSet();
  var duplicates = uniqueChars.where((char) => text.toLowerCase().split(char).length > 2);
  return duplicates.length;
}