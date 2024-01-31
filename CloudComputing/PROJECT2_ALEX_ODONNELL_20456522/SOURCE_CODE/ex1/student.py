import pika
import json,os
    
#local
connection = pika.BlockingConnection(
pika.ConnectionParameters(host=os.environ.get("RABBITMQ_HOSTNAME", "localhost"),
                credentials=pika.PlainCredentials(os.environ.get("RABBITMQ_USERNAME", "guest"),
                os.environ.get("RABBITMQ_PASSWORD", "guest"))))

channel = connection.channel()

def sendAssignment(id, module, answers):
    
    assignment = json.dumps({
        'StudentID': id, 
        'module': module, 
        'answer': answers,
        'status':'submitted'
    })
    
    routing_key = module.replace(" ","_").lower()+'.submitted'
    channel.basic_publish(exchange='assignment_exchange',routing_key=routing_key, body=assignment)
    print(f"{module} Assignment sent for correction")

sendAssignment(1, "Cloud Computing", "answers")
sendAssignment(1, "Data Mining", "answers")

print("Assignment(s) sent for correction")
connection.close()