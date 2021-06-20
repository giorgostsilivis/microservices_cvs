import redis
r = redis.Redis()
# r = redis.Redis(host='localhost', port=6379, db=0)

def redis_in(data):

    # r.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"})
    import datetime as dt
    keymail = int(dt.datetime.now().timestamp()*100)
    r.set(keymail,data)

    print(r.get(keymail).decode('utf-8'))

def redis_out():
    try:
        keys = r.keys('*')
        print(keys)
        maxkey = 0
        maxkeyb = ''
        for i in keys:
            if int(i) > maxkey:
                maxkey = int(i)
                maxkeyb = i
        # for key in keys:
        #     type = r.type(key).decode('utf-8')
        #     print(type)
        #     if type == "string":
        #         data = r.get(key)
        #         # print(r.get(data).decode('utf-8'))
        #         print(data.decode('utf-8'))
        data = r.get(maxkeyb)
        print(data.decode('utf-8'))
        return data.decode('utf-8')
    except:
        pass
