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

# To delete value
redis_conn.delete('name')

### Hash Commands
redis_conn.hset('person', # Key
    mapping = { 
        'name': 'Dmitrii', # field : value
        'age': '25', 
        'city': 'New York'
    }
)

value = redis_conn.hget('person', 'name').decode('utf-8')

redis_conn.hdel('person', 'city')

## Search by existence
elem = redis_conn.exists('name')
print(elem)

elem2 = redis_conn.hexists('person', 'name')
print(elem2)