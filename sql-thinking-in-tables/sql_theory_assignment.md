## 1. Why databases are important in real-world AI systems

Databases are important in AI systems because they store and organize the data that models depend on. AI doesn’t work without data, and in real-world applications, this data can be large, messy, and constantly changing.

Typical data stored includes user information (like names, preferences), transaction records, logs of user activity, and even datasets like images or text used for training models.

Structured storage is necessary because it keeps the data consistent and easy to access. Without structure, it becomes difficult to query, clean, or process data efficiently, which directly affects the performance of AI systems.

---

## 2. Relational database mental model

A relational database stores data in tables. Each table is made up of rows and columns.

* A table represents a single entity (for example, users or orders)
* A row represents one record (one user)
* A column represents an attribute (like name or email)

Each table should represent a single entity to avoid mixing unrelated data. This makes the database easier to understand, reduces duplication, and helps maintain clean relationships between different pieces of data.

---

## 3. Primary key

A primary key is a column used to uniquely identify each record in a table.

It must be unique so that no two records are the same, and it must be non-null because every record needs an identifier.

Primary keys are important because they allow us to reliably find and reference specific records. They are also used to connect tables with each other.

---

## 4. Database schema

A database schema is the structure or design of the database.

It defines what tables exist, what columns they have, the data types of those columns, and any rules like primary keys or constraints.

Schemas are important because they ensure that data is stored in a consistent format. They also make it easier for developers to understand and maintain the database.

---

## 5. Relationships between tables

In relational databases, tables are connected using foreign keys.

A foreign key is a column in one table that refers to the primary key of another table.

For example, a users table might store user details, and an orders table might store orders. The orders table can include a user_id column that links each order to a specific user.

This allows data to be connected without duplication and makes it possible to run queries that combine information from multiple tables.
