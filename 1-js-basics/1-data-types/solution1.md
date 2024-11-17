# Solution for 1: data types

The question is quite simple. We need to mention the data types that we would need to complete a shopping experience.

The experience can be divided into 5 different parts:

## User Login detials
| Name (property) | Data Type | Reason |
| --- | --- |
| id | String | - Unique identifier for the user. <br> - String is used as it will be a combination of letters and numbers |
| name | String | - Name of Customer <br> - String is used to store names |
| email | String  | - authentication <br> - combination of letters, numbers and special characters.|
| isLoggedIn | Boolean  | - check the status of a seesion <br> - a user can be loggedin or not thus boolean |

## Product Information
| Name (property) | Data Type | Reason |
| --- | --- |
| id | String | - Unique identifier for the each product. <br> - String is used as it will be a combination of letters and numbers |
| name | String | - Name of Product <br> - String is used to store names |
| price | Double  | - represnts cost of the product <br> - number to perform final cost calculations.|
| quantity |  Integer  | - number of products available |
| isAvailable | Boolean | - checks if a product is available or not <br> - a product can be available or not, thus boolean |

## Shopping Cart
| Name (property) | Data Type | Reason |
| --- | --- |
| items | Array | - holds all the products added to the cart |
| totalPrice | Double | - Sum of Prices will be double |
| discount |  Double  | - Stores discount percentage or amount |

## Payment Details
| Name (property) | Data Type | Reason |
| --- | --- |
| cardNumber | String | - Allows payment processing systems to validate it <br> - It will be with numbers and dashes |
| totalPaid | Double | - Reflects the final amount after discounts |

## Order Summary
| Name (property) | Data Type | Reason |
| --- | --- |
| orderId | String | - Unique identifier for each order |
| items | Array | - Lists purchased products |
| totalPrice | Double | - Reflects the amount charged |
| deliveryDate |  String  | - Displays estimated delivery date |