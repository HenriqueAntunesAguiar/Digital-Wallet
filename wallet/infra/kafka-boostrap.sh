set -e

echo "Criando Tópico transaction_requested"

kafka-topics \
  --bootstrap-server kafka:29092 \
  --create \
  --if-not-exists \
  --topic transaction_requested \
  --partitions 1 \
  --replication-factor 1

echo "Tópico transaction_requested Criado"