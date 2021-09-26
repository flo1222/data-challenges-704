## Background & Objectives

In the section we will discover subquery-refactoring! Indeed we may need to nest previous SQL queries coded into a new one to reduce repetition and simplify complex SQL statements. This is performed by the `WITH`. 👌

## Specs

### Average per Customer

👉 Implement `get_average_purchase` to get the average amount spent per order for each customer, ordered by customer ID.

### General Average

👉  Implement `get_general_avg_order` to get a `float` representing the average amount spent per order.


### Who are the best buyers?

Now let's find the customers who spent more than the average, that is their average amount spent per order is greater than the general average amount spent per order.

Can you see that the main part has already been done in the 2 previous questions? Let's use our previous queries thanks to the `WITH` clause.

👉 Implement the function `display_best_buyers` to get all the ID's and the average amount of these best buyers!

You should get this:

```python
display_best_buyers(db)
=> [(1031.24, 2), [...], (1096.3, 5)]
```

Meaning that the customer with ID 2 spent on average €1031.24 per order
