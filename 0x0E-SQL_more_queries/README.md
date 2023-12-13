# SQL - More queries

1. How to create a new MySQL user:
   To create a new MySQL user, you can use the following SQL command:
   ````sql
   CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
   ```
   Replace `'username'` with the desired username and `'password'` with the corresponding password for the user. The `'localhost'` part specifies the user's host, which can be modified depending on where you want the user to connect from.

2. How to manage privileges for a user to a database or table:
   To manage privileges for a user, you can use the `GRANT` statement. Here's an example of granting all privileges on a specific database to a user:
   ````sql
   GRANT ALL PRIVILEGES ON database_name.* TO 'username'@'localhost';
   ```
   Replace `'database_name'` with the name of the database, `'username'` with the desired username, and `'localhost'` with the appropriate host. You can also grant specific privileges like `SELECT`, `INSERT`, `UPDATE`, `DELETE`, etc., instead of granting all privileges.

3. What's a PRIMARY KEY:
   A PRIMARY KEY is a column or a set of columns in a table that uniquely identifies each row. It ensures that each row in the table has a unique identifier. The PRIMARY KEY constraint guarantees the uniqueness and integrity of the data in the table.

4. What's a FOREIGN KEY:
   A FOREIGN KEY is a column or a set of columns in a table that refers to the PRIMARY KEY of another table. It establishes a relationship between two tables, known as a parent-child relationship. The FOREIGN KEY constraint ensures referential integrity, meaning that values in the referencing column(s) must exist in the referenced table's PRIMARY KEY column(s).

5. How to use NOT NULL and UNIQUE constraints:
   The `NOT NULL` constraint ensures that a column cannot have a NULL (empty) value. It enforces that the column must always contain a value.

   The `UNIQUE` constraint ensures that all values in a column (or a combination of columns) are unique across the table. It prevents duplicate values from being inserted into the specified column(s).

6. How to retrieve data from multiple tables in one request:
   To retrieve data from multiple tables in one request, you can use JOIN operations. The JOIN operation combines rows from two or more tables based on a related column between them. The most commonly used JOIN types are INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL JOIN.

7. What are subqueries:
   Subqueries, also known as nested queries, are queries that are embedded within another query. They allow you to perform queries within queries, providing a way to retrieve data or perform calculations based on the results of another query. Subqueries can be used in SELECT, INSERT, UPDATE, or DELETE statements.

8. What are JOIN and UNION:
   JOIN is an operation used to combine rows from two or more tables based on a related column between them. It allows you to retrieve data from multiple tables based on common values in the related columns.

   UNION is used to combine the result sets of two or more SELECT statements into a single result set. It concatenates rows from different SELECT statements into a single result set, removing duplicate rows by default. The number of columns and their data types must match in all SELECT statements being combined with UNION.
