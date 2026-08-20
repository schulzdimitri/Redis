import redis

redis_conn = redis.Redis(
    host = 'redis',
    port = 6379,
    db = 0
)

# To insert and update values
redis_conn.set('name', 'Dmitrii')   

# To get value
my_value = redis_conn.get('name')
print(my_value.decode('utf-8'))
print(type(my_value))

# To delete value
redis_conn.delete('name')

