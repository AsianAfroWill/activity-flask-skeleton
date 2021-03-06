# Prereq

Install Postgres
https://www.postgresql.org/download/

```
sudo apt install postgresql
```

Install dependencies

```
sudo apt install python3-flask
sudo apt install libpq-dev
```

Install pip3 things
```
pip3 install sqlalchemy
pip3 install psycopg2
```

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

# Interview expectations

1. Create a schema
2. Create API handlers
3. Save/retrieve data to Postgres
4. Implementation collation algorithm
5. Handle message, passing through RabbitMQ

# Expected data

```
{
  timestamp: number,
  throughput: number,
  client: string,
  path: string
}
```
