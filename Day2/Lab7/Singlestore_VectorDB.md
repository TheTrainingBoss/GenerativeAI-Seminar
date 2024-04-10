## Creating a Vector Database in SingleStore

In this lab, you will create a Vector database in SingleStore and load data into it. You will also learn how to query the data in the Vector database.

### Step 1: Create a SingleStore account

1. Go to the [SingleStore website](https://www.singlestore.com/) and create an account.
2. Once you have created an account, log in to the SingleStore portal.
3. Create a new SingleStore cluster in Azure or AWS, your choice with a free utility tier.
4. Once the cluster is created, click on the cluster to open the SingleStore Studio and create a Workspace
5. In the Workspace, create a new database and name it `OpenAI-DB`.
6. Switch in Settings to the old UI and create a new table in the database with the following schema:
```sql
  CREATE TABLE IF NOT EXISTS myVectorTable(
    text TEXT,
    vector BLOB
);
```

### Step 2: Load data into the Vector database

```sql
INSERT INTO myVectorTable(text, vector) VALUES ("Once upon a time, there was a little dog named Fido.", JSON_ARRAY_PACK("
[<copy and paste the vector here>]
"));
```

### Step 3: Query the data in the Vector database
```sql
SELECT text, dot_product(vector, JSON_ARRAY_PACK("
[<copy and paste the vector here> ]")) as score
from myVectoreTable
order by score desc
limit 5
```