# Complex Data Management Assignment

This project implements three programs for processing queries over relational data stored in CSV files. It was developed for the course **ΜΥΕ041 - ΠΛΕ081: Διαχείριση Σύνθετων Δεδομένων** at the University of Ioannina.

## Contents

- `group_by_aggregation.py`: Implements group-by with aggregation using a variation of MergeSort.
- `merge_join.py`: Performs a natural join using the merge join algorithm.
- `composite_query.py`: Evaluates a composite query combining selection, join, and aggregation.

## Input data:
- `R.csv`: Table `R` with attributes `(A, B, C)` — columns 0, 1, 2 respectively.
- `S.csv`: Table `S` with attributes `(D, A, E)` — columns 0, 1, 2 respectively.

## Requirements

- Python 3.x
- No use of `pandas` or interactive environments like IPython (per assignment restrictions)

## Part 1: Group-by with Aggregation

This program calculates aggregate values (`sum`, `min`, or `max`) on one column grouped by another, using a variation of the **MergeSort** algorithm.

### Functionality

The program:
- Accepts a CSV file (`R.csv` or `S.csv`) as input.
- Groups the data by a specified attribute (column index).
- Applies an aggregate function to another attribute.

### Usage

```bash
python group_by_aggregation.py <input_file.csv> <group_by_attr> <agg_attr> <agg_function>
```

- `<input_file.csv>`: Input data file, e.g., `R.csv` or `S.csv`
- `<group_by_attr>`: Index of the grouping attribute (0, 1, or 2)
- `<agg_attr>`: Index of the aggregation attribute (0, 1, or 2)
- `<agg_function>`: One of `sum`, `min`, or `max`

### Example

```bash
python group_by_aggregation.py R.csv 1 2 max
```

This computes:

```sql
SELECT R.1, MAX(R.2)
FROM R
GROUP BY R.1
```

### Output (`O1.csv`)

The output contains:

```
<group_value>,<aggregate_result>
```

Example:

```
1,10
2,10
3,10
4,9
5,10
```

---

## Part 2: Merge Join

This program implements a **natural join** between two sorted relations `R` and `S` using the **merge join algorithm**.

### Input Schemas

- `R.csv`: (A, B, C) → columns 0, 1, 2
- `S.csv`: (D, A, E) → columns 0, 1, 2
- `R.A` is a **primary key**
- `S.A` is a **foreign key** referencing `R.A`
- Both files are sorted on attribute `A`

### Usage

```bash
python merge_join.py
```

No arguments needed. Make sure `R.csv` and `S.csv` exist in the directory.

### Output (`O2.csv`)

Each row of the output has the schema:

```
A,B,C,D,E
```

### Example Output

```
45,41,7,1,3
45,41,7,2,9
45,41,7,3,7
45,41,7,4,6
45,41,7,5,4
```

---

## Part 3: Composite Query

This program evaluates the following SQL-like query in a **single pass** without full file loading:

```sql
SELECT S.A, SUM(S.E)
FROM R, S
WHERE R.A = S.A AND R.C = 7
GROUP BY S.A
```

### Usage

```bash
python composite_query.py
```

No arguments needed. Input files `R.csv` and `S.csv` must be in the same folder.

### Output (`O3.csv`)

Each row contains:

```
A,SUM_E
```

### Example Output

```
45,63
47,44
78,60
187,70
501,55
```

---
## Author

- Themistokleia Siakavara
---
