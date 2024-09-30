/**
 * it will be possible to add arbitrary elements to it (add method)
    an attempt to add an element that is already in the object will be ignored;
    it will be possible to check whether an element is present in the object (has method)
    it will be possible to delete an element (del method)
    it will be possible to check the number of elements (length property)
    it will be possible to use any technique for passing elements of an iterable object (spread operator, for ... of, iterators), and an appropriate generator should be used in the implementation.
 */

class MyIterable {
	list = [];
	constructor() {}

	get length() {
		return this.list.length;
	}

	add(n) {
		for (let item in this.list) {
			if (item == n) {
				return;
			}
		}
		this.list.push(n);
	}

	del(n) {
		let index;
		for (let i = 0; i < this.list.length; i++) {
			if (this.list[i] == n) {
				index = i;
			}
		}
		this.list.splice(index, 1);
	}

	has(n) {
		return this.list.indexOf(n) != -1 ? true : false;
	}

	[Symbol.iterator]() {
		let index = 0;
		let list = this.list;
		return {
			next: function () {
				if (index < list.length) {
					return { value: list[index++], done: false };
				} else {
					return { value: undefined, done: true };
				}
			},
		};
	}
}

let iterable = new MyIterable();
iterable.add(2);
iterable.add(5);
iterable.add(3);
iterable.add(2);
iterable.del(3);

console.log(iterable.length); // -> 2
console.log(iterable.has(2)); // -> true
console.log(iterable.has(3)); // -> false
console.log(...iterable); // -> 2 5
