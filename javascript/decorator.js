/**
 *
    Write a decorator named myDecorator that will store the arguments of the decorated function call.

    If the function has already been called with these arguments, an appropriate message should appear in the console containing, among other things, the values of those arguments.

    Note – the function can be called with any number of arguments, so use rest arguments for this purpose.

    Test the decorator using the following code:
 */
let myDecorator = function (fn) {
	const calls = new Set();
	return function (...args) {
		const argsKey = JSON.stringify(args);
		if (calls.has(argsKey)) {
			return `Arguments already used: ${args}`;
		}
		calls.add(argsKey);
		return fn(...args);
	};
};

let sum = function (...args) {
	let retVal = 0;
	for (let arg of args) {
		retVal += arg;
	}
	return retVal;
};

let dfn = myDecorator(sum);
console.log(dfn(2, 3, 4)); // -> 9
console.log(dfn(4, 5)); // -> 9
console.log(dfn(2, 3, 4)); // -> Arguments already used: 2,3,4
console.log(dfn(4, 5)); // -> Arguments already used: 4,5
