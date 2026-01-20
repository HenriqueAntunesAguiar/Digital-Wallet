1️⃣ Problema de negócio do projeto
Problema

Uma fintech precisa oferecer uma carteira digital para seus clientes, permitindo:

movimentação de saldo

controle de limites

registro de transações

geração de extratos

alta confiabilidade e consistência

desacoplamento entre domínios

O sistema precisa ser escalável, orientado a eventos e preparado para crescimento, pois o volume de transações pode aumentar rapidamente.

2️⃣ Contexto do mundo real (importante)

Imagine este cenário:

O sistema precisa processar milhares de transações simultâneas, manter consistência financeira, permitir evolução independente dos domínios e garantir que falhas em um serviço não derrubem o sistema inteiro.

Esse contexto força decisões arquiteturais maduras.

3️⃣ Bounded Contexts (domínios)

Você terá 4 domínios independentes, cada um com responsabilidade clara:

🟣 1. Wallet (core do sistema)

Responsabilidade

Manter saldo da carteira

Aplicar débitos e créditos

Garantir invariantes financeiras

Regras

Saldo nunca pode ser negativo

Operações devem ser idempotentes

Alterações de saldo geram eventos

📌 Esse é o coração do sistema

🟣 2. Transactions

Responsabilidade

Registrar todas as movimentações

Garantir histórico imutável

Atribuir status às transações

Regras

Transações são imutáveis

Uma transação nasce como PENDING

Pode evoluir para COMPLETED ou FAILED

Consome eventos do Wallet

🟣 3. Limits

# Responsabilidade

Controlar limites de gasto

Validar se uma operação é permitida

Evoluir regras sem impactar Wallet

# Regras

Limite diário/mensal

Limites independentes do saldo

Deve responder rapidamente

# 📌 Esse serviço NÃO deve conhecer o Wallet internamente

🟣 4. Statements (somente leitura)

# Responsabilidade

Gerar extratos

Consolidar dados

Otimizado para leitura

# Regras

Event-driven

Dados derivados (read model)

Pode ficar inconsistente temporariamente (eventual consistency)

4️⃣ O PROBLEMA CENTRAL (resumido)

Como construir uma plataforma de carteira digital distribuída, escalável e resiliente, onde cada domínio evolui de forma independente, mantendo consistência financeira e alta confiabilidade?

Esse problema não pode ser resolvido com CRUD simples.

5️⃣ Por que esse problema exige tudo que a vaga pede
✔️ Microservices

Domínios independentes

Deploy separado

Escala isolada

✔️ Arquitetura Hexagonal

Cada serviço terá:

Domain

Application

Adapters (REST, Messaging, Persistence)

Framework vira detalhe.

✔️ Comunicação assíncrona

Wallet emite eventos

Transactions, Limits e Statements consomem

Falhas isoladas

✔️ Large-scale thinking

Idempotência

Eventual consistency

Read vs Write models

Falhas parciais

✔️ Clean boundaries

Nenhum serviço acessa DB de outro

Comunicação via contratos

Domínio isolado

6️⃣ Critérios de avaliação (use isso como checklist)

Se seu projeto responder “sim” para isso, ele está nível Nubank:

 Cada serviço tem domínio isolado?

 Regras estão no domínio, não no controller?

 Existe comunicação via eventos?

 Falhas são tratadas?

 README explica decisões?

 Testes cobrem regras críticas?

 Arquitetura não depende do Django?

7️⃣ Próximo passo (natural)

Agora você pode escolher:

👉 Opção A

Você propõe a arquitetura da solução (em texto)
Eu reviso e ajusto como se fosse uma code review de Nubank.

👉 Opção B

Eu desenho a arquitetura base (serviços, camadas e comunicação)
E você implementa em cima.

📌 Sugestão: comece pela Opção B, para não errar o escopo.

👉 Qual você prefere?