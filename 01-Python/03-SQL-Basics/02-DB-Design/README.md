## Background & Objectives

The goal of this first challenge is to become familiar with database design, *a* crucial skill to make your backend maintainable, flexible and efficient.

## Specs

#### E-commerce database design

There are many ways to build an e-commerce database, but let's start by building a basic system with `customers`, `products` and `orders`.

Here are the requirements of our system:

- A `customer` has a `first_name`, `last_name`, an `email` and a `city`.
- A `product` has a `name` and a `unit_price`.
- An `order` is defined by a `date_of_order`.
- An `order` is created by only one `customer`.
- A `customer` can make many `orders`.
- An `order` can have many `products`.
- A `product` can be in many `orders`.
- A given `order` can have the same `product` multiple times so we need to record the `quantity` for a given `product` per `order`.

<details><summary markdown='span'>💡 Hint</summary>
  You need to introduce a join table <code>product_orders</code>.

</details>

#### Design the schema

Design a database schema for an-ecommerce app that meets the requirements.
For this, you must use the [SQL Designer](http://db.lewagon.com).
To check your solution, click on "Save / Load", then "Save XML", copy/paste the generated XML code in `ecommerce.xml`. You can then `make` to check your solution.

## Key learning points

- Do you know what a schema is?
- What's the relation between tables?
- Could you draw the database schema behind facebook? airbnb? Take a sheet of paper and have a go!
