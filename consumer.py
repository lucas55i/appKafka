from kafka import KafkaConsumer

# Configurações do Kafka
config = {
    "bootstrap_servers": "localhost:9092",  # substitua com o endereço do seu broker Kafka
    "group_id": "1",  # atribua um ID de grupo exclusivo
    "auto_offset_reset": "earliest"  # comece a consumir mensagens desde o início do tópico em caso de falta de commit
    # adicione outras configurações conforme necessário
}

topic = 'lucas'

# Criar consumidor Kafka
consumer = KafkaConsumer(topic, **config)

# Loop de leitura de mensagens
for mensagem in consumer:
    # Processar a mensagem
    print("Mensagem recebida: {}".format(mensagem.value.decode("utf-8")))

# Fechar o consumidor
consumer.close()
