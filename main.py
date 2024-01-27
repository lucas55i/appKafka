from kafka import KafkaProducer

# Configurações do Kafka
config = {
    'bootstrap_servers': 'localhost:9092',  # substitua com o endereço do seu broker Kafka
    # adicione outras configurações conforme necessário
}

# Criar produtor Kafka
producer = KafkaProducer(**config)

# Tópico para o qual você deseja enviar mensagens
topic = 'lucas'

# Mensagem a ser enviada
mensagem = 'Olá, Kafka!'

# Enviar mensagem para o tópico
producer.send(topic, mensagem.encode('utf-8'))

# Fechar o produtor
producer.close()