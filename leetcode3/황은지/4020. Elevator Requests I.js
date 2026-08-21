/**
 * @param {number} n
 * @param {number[]} requests
 * @return {number}
 */
var elevatorRequests = function (n, requests) {
  let seconds = 0;

  for (let i = 0; i < requests.length; i++) {
    if (i !== 0) seconds += Math.abs(requests[i] - requests[i - 1]);
    else seconds += requests[i];
  }

  return seconds;
};
