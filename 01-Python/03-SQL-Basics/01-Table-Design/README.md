## Setup

The `make` relies on external [`lxml`](https://pypi.org/project/lxml/) and [`pyyaml`](https://pypi.org/project/pyyaml/) packages to read the XML from the SQL Designer tool. In the terminal, run:

```bash
pip install lxml pyyaml
```

## Background & Objectives

The goal of this first challenge is to create our first table using the [SQL Designer](https://kitt.lewagon.com/db/new).

## Specs

### Designing our first table

Let's create a table to store customers. The table should have these columns:

- first_name
- last_name
- email
- city

NOTE: Remember, all of our tables will also have an `id` column!

### Drawing the table

Use the [SQL Designer](https://kitt.lewagon.com/db/new) to draw the `customers` table with the columns specified above.
To check your solution, click on "Save / Load", then "Save XML", copy/paste the generated XML code in `customers.xml`. You can then `make` to check your solution.

## Key learning points

- Become comfortable with using the [SQL Designer](https://kitt.lewagon.com/db/new) tool to build your schema.
- Use the correct conventions when naming tables and columns in your schema.
