
var _ = {
   map: function(array, callback) {
      for (var num = 0; num<array.length; num++) {
         array[num] = callback(array[num]);
      }
      return array;
   },
   reduce: function(array, callback, memo) {
      var sum = memo;
      for (var num = 0; num<array.length; num++) {
         sum+=array[num];
      }
      return sum;
   },
   find: function(array, callback) {
      for (var num = 0; num<array.length; num++) {
         if (callback(array[num]) === true) {
            return array[num];
         }
      }
   },
   filter: function(array, callback) {
      var array2 = [];
      for (var num = 0; num<array.length; num++) {
         console.log(callback(array[num]));
         if (callback(array[num]) === true) {
            array2.push(array[num]);
         }
      }
      return array2;
   },
   reject: function(array, callback) {
      var array2 = [];
      for (var num = 0; num<array.length; num++) {
         console.log(callback(array[num]));
         if (callback(array[num]) !== true) {
            array2.push(array[num]);
         }
      }
      return array2;
   },
};

var cobalt = _.map([1, 2, 3], function(num){ return num * 3; });
console.log(cobalt);

var aluminum = _.filter([1, 2, 3, 4, 5, 6], function(num){ return num % 2 === 0; });
console.log(aluminum);

var germanium = _.reduce([1, 2, 3, 4, 345, 35, 34, 543, 345, 435], function(memo, num){ return memo + num; }, 0);
console.log(germanium);

var zinc = _.find([1, 1, 3, 4, 5, 6], function(num){ return num % 2 === 0; });
console.log(zinc);

var yterbium = _.reject([1, 2, 3, 4, 5, 6], function(num){ return num % 2 === 0; });
console.log(yterbium);
