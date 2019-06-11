# Prereq

Install Postgres
https://www.postgresql.org/download/

# To run

## Flask

```python
. bin/activate
export FLASK_APP=hello.py
flask run
```

## Postgres

```
initdb post.db
pg_ctl -D post.db -l logfile start
psql postgres
```

```sql
create table activities ( timestamp integer, throughput integer, client varchar(255), path varchar(65535) );
```

# Interview expectations

1. Create a schema
2. Create API handlers
3. Save/retrieve data to Postgres
4. Implementation collation algorithm
5. Handle message, passing through RabbitMQ

# Expected data

```json
{
  timestamp: number,
  throughput: number,
  client: string,
  path: string
}
```
