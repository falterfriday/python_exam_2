module.exports = {
	add: function(num1, num2) {
		console.log("The sum is:", num1+num2);
	},
	multiply: function(num1, num2) {
		console.log("The product is:", num1*num2);
	},
	square: function(num) {
		console.log("The square is:", num*num);
	},
	random: function(num1,num2) {
		var num = Math.floor((Math.random()*(num2 - num1))+num1);
		console.log("Your random number is:", num);
	}
};
