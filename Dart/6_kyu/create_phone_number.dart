String createPhoneNumber(List numbers) {
   String formattedNumber = '(${numbers.sublist(0, 3).join()}) ${numbers.sublist(3, 6).join()}-${numbers.sublist(6).join()}';
  return formattedNumber;
}