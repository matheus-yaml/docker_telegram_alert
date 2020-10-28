import os
import socket
hostname = socket.gethostname()

os.system(""" free -m |grep Mem | awk '{print $7}' > data.txt""")
mem_livre = 0
for c in  open('data.txt', 'r'):
 	mem_livre = int(c)
 	break

os.system(""" free -h |grep Mem | awk '{print $2}' > data.txt""")
mem_total = ''
for c in  open('data.txt', 'r'):
 	mem_total = c.replace('\n', '')
 	break


if mem_livre <  500: 
	os.system("""docker stats --no-stream > docker.txt""")		
	
	lista = f'{"-"*90}\nALERTA: \nMemória livre < 500MB em {hostname}\nMemória total: {mem_total}\nUSO DE CONTAINERS:\n'
	for c in  open('docker.txt', 'r'):
		lista += c

os.system(f"""
	curl -X POST \
	-H 'Content-Type: application/json' \
	-d '{{"chat_id": "xxxxxxxxxx", "text": "{lista}", "disable_notification": false}}' \
	https://api.telegram.org/botxxxxxxxxxxx:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx/sendMessage  """)


