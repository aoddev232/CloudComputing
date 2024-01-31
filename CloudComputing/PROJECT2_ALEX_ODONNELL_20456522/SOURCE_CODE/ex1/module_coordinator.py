import pika, sys, os,json

def main():
    #local
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=os.environ.get("RABBITMQ_HOSTNAME", "localhost"),
                    credentials=pika.PlainCredentials(os.environ.get("RABBITMQ_USERNAME", "guest"),
                    os.environ.get("RABBITMQ_PASSWORD", "guest"))))
    
    channel = connection.channel()

    channel.exchange_declare(exchange='assignment_exchange',exchange_type='fanout')
    channel.queue_declare(queue='cloud_queue')
    channel.queue_bind(exchange='assignment_exchange',queue='cloud_queue', routing_key='cloud_computing.submitted')
    channel.queue_declare(queue='data_mining_queue')
    channel.queue_bind(exchange='assignment_exchange',queue='data_mining_queue', routing_key='data_mining.submitted')
    channel.queue_declare(queue='validation_queue')
    channel.queue_bind(exchange='assignment_exchange',queue='validation_queue', routing_key='*.corrected')
    channel.queue_declare(queue='result_queue')
    channel.queue_bind(exchange='assignment_exchange',queue='result_queue')

    def callback(ch, method, properties, body):
        assignment = json.loads(body)
        if(assignment['status']=='validated'):
            print("Received "+str(assignment['StudentID'])+ "," + str(assignment['module']) + ","+str(assignment['status'])+", and submit it to Brightspace")
            print("Publishing Assignment...")
            assignment['status']='published'
            print("Assignment Published")

    channel.basic_consume(queue='result_queue', on_message_callback=callback, auto_ack=False)
    print(' [*] Module Coodinator is Waiting...')
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