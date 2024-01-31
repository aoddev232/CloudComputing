import pika, sys, os,json

def main():
    #local
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=os.environ.get("RABBITMQ_HOSTNAME", "localhost"),
                   credentials=pika.PlainCredentials(os.environ.get("RABBITMQ_USERNAME", "guest"),
                   os.environ.get("RABBITMQ_PASSWORD", "guest"))))

    channel = connection.channel()

    def callback(ch, method, properties, body):
       
        assignment = json.loads(body)
        if (assignment['module']=='Cloud Computing' and assignment['status'] == 'submitted'):
            print("Received Student "+str(assignment['StudentID'])+"'s Assignment for "+str(assignment['module'])+" as "+str(assignment['status']))
            print("Correcting Assignment...")
            assignment['status']='corrected'
            print("Assignment Corrected")
            routing_key = assignment['module'].replace(" ","_").lower()+'.corrected'
            print("Sending Assignment for to TA for Validation...")
            channel.basic_publish(exchange='assignment_exchange',routing_key=routing_key,body=json.dumps(assignment))
            print("Assignment Sent for Validation")
    
    channel.basic_consume(queue='cloud_queue', on_message_callback=callback, auto_ack=False)
    print(' [*] Cloud Computing Demonstrator is Waiting...')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)