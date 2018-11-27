import redis

try:
	debug = True
	
	redis_host = "host"
	redis_port = 6380
	redis_pass = "pass"
	redis_ssl = False
	redis_ssl_certs = ""
	
	list_name = "my_list"
	ltrim_start = 0
	ltrim_stop = 1000
	
	if (redis_ssl):
		if (debug):
			print("Attempting SSL Connection To Redis");
			
		conn = redis.StrictRedis(
			host=redis_host,
			port=redis_port,
			password=redis_pass,
			ssl=redis_ssl,
			ssl_ca_certs=redis_ssl_certs)	
	else:
		if (debug):
			print("Attempting NON-SSL Connection To Redis");
	
		conn = redis.StrictRedis(
			host=redis_host,
			port=redis_port,
			password=redis_pass)
	

	if (debug):
		if(conn.ping()):
			print("Connected To Redis");
		else:
			exit("Not Connected To Redis")

	list_len = conn.llen(list_name)
	
	if(debug):
		print("LLEN FOR " + list_name + ": " + str(list_len))
		
	ltrim_respone = conn.ltrim(list_name, ltrim_start, ltrim_stop)	

	if(debug):
		print("LTRIM RESPONSE " + str(ltrim_respone))
		
	conn.disconnect()
	
	if (debug):
		print("Disconnecting From Redis");
	
except Exception as ex:
    print 'Error:', ex
    exit('Failed to connect, terminating.')

