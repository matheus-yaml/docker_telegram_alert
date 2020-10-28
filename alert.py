import os
import socket
hostname = socket.gethostname()

token = 'bot9999999999:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
chat_id = '-9999999999'

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

if mem_livre: # <  500: 
	os.system("""docker stats --no-stream > data.txt""")		
	
	lista = f'{"-"*90}\nALERTA: \nMemória livre = {mem_livre}MB em {hostname.upper()}\nMemória total: {mem_total}\nCONTAINERS ↓↓↓:\n'
	# for c in  open('data.txt', 'r'):
		# lista += c

	os.system(f"""
		curl -X POST \
		-H 'Content-Type: application/json' \
		-d '{{"chat_id": "{chat_id}", "text": "{lista}", "disable_notification": false}}' \
		https://api.telegram.org/{token}/sendMessage  """)
	
	import image
	image.criar()

	os.system(f"""curl -F document=@"data.png" https://api.telegram.org/{token}/sendDocument?chat_id={chat_id}""")
	os.system(""" rm data.png """)
	os.system(""" rm data.txt """)





