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
        if(assignment['status']=='corrected'):
            print("Received "+str(assignment['StudentID'])+","+str(assignment['status'])+","+str(assignment['module']))
            print("Validating Assignment...")
            assignment['status']='validated'
            print("Assignment Validated")
            channel.basic_publish(exchange='assignment_exchange',routing_key=str(assignment['module'])+'.validated',body=json.dumps(assignment))
            print("Assignment send to Module Coordinator")    

    channel.basic_consume(queue='validation_queue',on_message_callback=callback, auto_ack=False)
    print(' [*] Teaching assistant is Waiting...')
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