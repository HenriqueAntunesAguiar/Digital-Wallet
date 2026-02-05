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

echo "Criando Tópico limit_approved"

kafka-topics \
  --bootstrap-server kafka:29092 \
  --create \
  --if-not-exists \
  --topic limit_approved \
  --partitions 1 \
  --replication-factor 1

echo "Tópico limit_approved Criado"

echo "Criando Tópico limit_denied"

kafka-topics \
  --bootstrap-server kafka:29092 \
  --create \
  --if-not-exists \
  --topic limit_denied \
  --partitions 1 \
  --replication-factor 1

echo "Tópico limit_denied Criado"

echo "Criando Tópico wallet_approved"

kafka-topics \
  --bootstrap-server kafka:29092 \
  --create \
  --if-not-exists \
  --topic wallet_approved \
  --partitions 1 \
  --replication-factor 1

echo "Tópico wallet_approved Criado"

echo "Criando Tópico wallet_denied"

kafka-topics \
  --bootstrap-server kafka:29092 \
  --create \
  --if-not-exists \
  --topic wallet_denied \
  --partitions 1 \
  --replication-factor 1

echo "Tópico wallet_denied Criado"

echo "Criando Tópico transaction_completed"

kafka-topics \
  --bootstrap-server kafka:29092 \
  --create \
  --if-not-exists \
  --topic transaction_completed \
  --partitions 1 \
  --replication-factor 1

echo "Tópico transaction_completed Criado"

echo "Criando Tópico transaction_pending"

kafka-topics \
  --bootstrap-server kafka:29092 \
  --create \
  --if-not-exists \
  --topic transaction_pending \
  --partitions 1 \
  --replication-factor 1

echo "Tópico transaction_pending Criado"

echo "Criando Tópico transaction_failed"

kafka-topics \
  --bootstrap-server kafka:29092 \
  --create \
  --if-not-exists \
  --topic transaction_failed \
  --partitions 1 \
  --replication-factor 1

echo "Tópico transaction_failed Criado"

echo "Criando Tópico create_wallet"

kafka-topics \
  --bootstrap-server kafka:29092 \
  --create \
  --if-not-exists \
  --topic create_wallet \
  --partitions 1 \
  --replication-factor 1

echo "Tópico create_wallet Criado"

echo "Criando Tópico update_limit"

kafka-topics \
  --bootstrap-server kafka:29092 \
  --create \
  --if-not-exists \
  --topic update_limit \
  --partitions 1 \
  --replication-factor 1

echo "Tópico update_limit Criado"

echo "Criando Tópico create_limit"

kafka-topics \
  --bootstrap-server kafka:29092 \
  --create \
  --if-not-exists \
  --topic create_limit \
  --partitions 1 \
  --replication-factor 1

echo "Tópico create_limit Criado"