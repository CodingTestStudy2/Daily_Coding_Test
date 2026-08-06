/**
 * @param {string[]} dictionary
 * @param {string} sentence
 * @return {string}
 */
var replaceWords = function (dictionary, sentence) {
  dictionary.sort((a, b) => a.length - b.length);
  const splited = sentence.split(" ");

  for (let i = 0; i < splited.length; i++) {
    const word = splited[i];
    for (let dicWord of dictionary) {
      if (word.startsWith(dicWord)) {
        splited[i] = dicWord;
        break;
      }
    }
  }

  return splited.join(" ");
};
