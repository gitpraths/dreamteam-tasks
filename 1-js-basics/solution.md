# Solution for JS-Basics

1. Sub Topic 1

Assignment:


# Solution for 1: data types

Everything that I studied, that is, all the theory with the programs is metioned in the excercise_.js file
I have also attached a js file to run and check the code.

The question is quite simple. We need to mention the data types that we would need to complete a shopping experience.

The experience can be divided into 5 different parts:

## User Login detials
| Name (Property) | Data Type | Reason                                                                                  |
|------------------|-----------|----------------------------------------------------------------------------------------|
| `id`            | String    | - Unique identifier for the user.                                                     <br> - String is used as it will be a combination of letters and numbers. |
| `name`          | String    | - Name of Customer.                                                                   <br> - String is used to store names. |
| `email`         | String    | - Authentication.                                                                     <br> - Combination of letters, numbers, and special characters. |
| `isLoggedIn`    | Boolean   | - Check the status of a session.                                                      <br> - A user can be logged in or not, thus Boolean. |

---

## Product Information
| Name (Property) | Data Type | Reason                                                                                  |
|------------------|-----------|----------------------------------------------------------------------------------------|
| `id`            | String    | - Unique identifier for each product.                                                 <br> - String is used as it will be a combination of letters and numbers. |
| `name`          | String    | - Name of Product.                                                                    <br> - String is used to store names. |
| `price`         | Double    | - Represents the cost of the product.                                                 <br> - Number is used to perform final cost calculations. |
| `quantity`      | Integer   | - Number of products available.                                                       |
| `isAvailable`   | Boolean   | - Checks if a product is available or not.                                            <br> - A product can be available or not, thus Boolean. |

---

## Shopping Cart
| Name (Property) | Data Type | Reason                                                                                  |
|------------------|-----------|----------------------------------------------------------------------------------------|
| `items`         | Array     | - Holds all the products added to the cart.                                           |
| `totalPrice`    | Double    | - Sum of prices will be a double.                                                     |
| `discount`      | Double    | - Stores discount percentage or amount.                                               |

---

## Payment Details
| Name (Property) | Data Type | Reason                                                                                  |
|------------------|-----------|----------------------------------------------------------------------------------------|
| `cardNumber`    | String    | - Allows payment processing systems to validate it.                                    <br> - It will be a combination of numbers and dashes. |
| `totalPaid`     | Double    | - Reflects the final amount after discounts.                                           |

---

## Order Summary
| Name (Property) | Data Type | Reason                                                                                  |
|------------------|-----------|----------------------------------------------------------------------------------------|
| `orderId`       | String    | - Unique identifier for each order.                                                    |
| `items`         | Array     | - Lists purchased products.                                                            |
| `totalPrice`    | Double    | - Reflects the amount charged.                                                         |
| `deliveryDate`  | String    | - Displays the estimated delivery date.                                                |

Challenge:

```
// 1. Case Sensitivity
let age = 1; 
let Age = 2; 
console.log(age == Age); // false
// JavaScript is case-sensitive, meaning age and Age are treated as entirely different variables.

// 2. Type Coercion
console.log(1 == '1'); // true
console.log(1 === '1'); // false
// == performs type coercion, converting '1' (string) to 1 (number) before comparing.
// === is a strict equality operator and doesn't perform type coercion, so it compares both value and type.

// 3. numm vs. undefined
console.log(null == undefined); // true
console.log(null === undefined); // false

// null and undefined are considered loosely equal (==) because they both represent "absence of value".
// They are not strictly equal (===) because null is an object type and undefined is a primitive type.

// 4. NaN is Not Equal to Itself
console.log(NaN == NaN); // false
console.log(NaN === NaN); // false
// NaN (Not-a-Number) is unique in that it is not equal to anything, including itself. Use Number.isNaN(value) to check for NaN.

// 5. Typeof Difference
console.log(typeof null); // "object"
console.log(typeof NaN); // "number"
// typeof null returns "object" because of a historical bug in JavaScript that was never fixed for backward compatibility.
// typeof NaN returns "number" because NaN is technically a special value of the number type.

```
2. Function Methods

Assignment:

```
# Solution for 2: Functions

Everything that I studied, that is, all the theory with the programs is metioned in the excercise_.js file
I have also attached a js file to run and check the code.

This assignment will familiarise you with the use of functions in different situations.
```
```
## Function that returns something:


function addNumbers(a, b) {
    return a + b;
}

// Example usage:
const result = addNumbers(1, 2);
console.log('Sum: ${result}'); // Output: Sum: 3


```
```
## Function that doesn't return anything
def greet_user(name):
function greetUser(name) {
    console.log('Hello, ${name}!');
}

// Example usage:
greetUser("Prarthana"); // Output: Hello, Prarthana!
```
```
## Function with no Parameters
function printMessage() {
    console.log("Dream Team Task: 04");
}
printMessage(); 

```
```
## Function with mix parameters
function introducePerson(name, age = 20, city = "Hyd") {
    return 'My name is ${name}, I am ${age} years old, and I live in ${city}.';
}
const intro1 = introducePerson("Prarthana");
console.log(intro1);

```
Challenge:

```
Functions are standalone blocks of code that perform tasks, while methods are functions associated with an object and can access and modify the object's data.

Functions are independent and can be called on their own, whereas methods are tied to objects and operate on the object's attributes.

```

3. Sub Topic 3

Assignment 3:

```
let allStudents = ['A', 'B-', 1, 4, 5, 2, 'C', 3, 'C-'];
let passedStudents = [];

for (let i = 0; i < allStudents.length; i++) {
    let grade = allStudents[i];
    if (typeof grade === 'number') {
        // First grading system (numeric grades)
        if (grade >= 3) {
            passedStudents.push(grade);
        }
    } else if (typeof grade === 'string') {
        // Second grading system (letter grades)
        if (grade === 'A' || grade === 'A-' || grade === 'B' || grade === 'B-' || grade === 'C') {
            passedStudents.push(grade);
        }
    }
}

console.log("Students who pass:", passedStudents);

```

Challenge:

```
function checkNumber(num) {
  let result;
  if (num > 0) {
      result = "Positive";
  } else if (num < 0) {
      result = "Negative";
  } else {
      result = "Zero";
  }
  return result;
}

console.log(checkNumber(5));  // Output: Positive
console.log(checkNumber(-3)); // Output: Negative
console.log(checkNumber(0));  // Output: Zero

function checkNumber1(num) {
  let result = num > 0 ? "Positive" : num < 0 ? "Negative" : "Zero";
  return result;
}

// Test
console.log(checkNumber1(5));  // Output: Positive
console.log(checkNumber1(-3)); // Output: Negative
console.log(checkNumber1(0));  // Output: Zero

// I prefer If..else..if (logical operator approach) as its easily understandable and readable.

```
4. Sub Topic 4

Assignment:

```
for (let i = 1; i <= 20; i += 3) {
    console.log(i);
}

```

Challenge:

```
// 1. forEach
iceCreamFlavors.forEach(flavor => {
    console.log(flavor);
});

// 2. for..of
for (const flavor of iceCreamFlavors) {
    console.log(flavor);
}

// 3. map
iceCreamFlavors.map(flavor => {
    console.log(flavor);
});

```