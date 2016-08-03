function fib() {
  var num = 0;
  var prev_num = 1;
  var temp;
  function nacci() {
    temp = num;
    num+= prev_num;
    prev_num = temp;
    console.log(num);
  }
  return nacci;
}
var fibCounter = fib();

fibCounter();
fibCounter();
fibCounter();
fibCounter();
fibCounter();
