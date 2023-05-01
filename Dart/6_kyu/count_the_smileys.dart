int countSmileys(List<String> arr) {
  int count = 0;
  for (String face in arr) {
    if (face.length == 2) {
      if ([':', ';'].contains(face[0]) && [')', 'D'].contains(face[1])) {
        count++;
      }
    } else if (face.length == 3) {
      if ([':', ';'].contains(face[0]) &&
          ['-', '~'].contains(face[1]) &&
          [')', 'D'].contains(face[2])) {
        count++;
      }
    }
  }
  return count;
}