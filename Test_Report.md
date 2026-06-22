# MongoDB Agentic Copilot Test Report

## Application

E-commerce Dataset

## OCS Schema

### customers

Fields:

* customer_id
* name
* email
* city

### products

Fields:

* product_id
* name
* category
* price
* stock

### orders

Fields:

* order_id
* customer_id
* product_id
* quantity
* order_date

## Relationships

customers → orders → products

## Test Cases

### Test 1: MongoDB Connection

Result: PASS

### Test 2: Collections Loaded

Result: PASS

### Test 3: Relationship Query

Query:
What products did Rahul buy?

Output:
Rahul bought Laptop, Mouse

Result: PASS

### Test 4: Generic Query using Ollama

Query:
What is MongoDB?

Result: PASS

## Conclusion

OCS schema verified successfully.

Relationship traversal and context-aware query execution are working correctly.

Generated and verified using E-commerce dataset.
