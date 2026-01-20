(br)
💳 Wallet – Sistema Distribuído de Carteira Digital (Showcase Arquitetural)
Visão Geral

Este projeto é um showcase arquitetural, criado para demonstrar pensamento de engenharia em nível sênior aplicado a um domínio financeiro.

O objetivo não é entregar um sistema de carteira pronto para produção, mas sim ilustrar como uma arquitetura distribuída e orientada a eventos pode ser desenhada para lidar com:

movimentação de saldo

ciclo de vida de transações

validação de limites

consistência eventual

isolamento de domínios

O foco está em limites claros, orquestração explícita e fluxo de eventos, e não em complexidade de infraestrutura.

Contexto do Problema

Uma fintech precisa oferecer uma carteira digital que suporte:

débito e crédito de saldo

limites diários e mensais

rastreabilidade de transações

consistência entre múltiplos serviços

escalabilidade e desacoplamento

Esse problema é intencionalmente modelado como múltiplos serviços independentes, cada um sendo dono de uma parte específica do domínio.

Objetivos Arquiteturais

Separação clara de responsabilidades

Limites de domínio bem definidos

Orquestração explícita

Sincronização de estado via eventos

Ausência de acoplamento implícito (ex: banco compartilhado)

Tratamento explícito de sucesso e falha

Serviços e Responsabilidades
🔹 Serviço de Pagamento (Orquestrador)

Ponto de entrada para requisições de pagamento

Coordena o fluxo

Chama outros serviços de forma síncrona quando uma decisão imediata é necessária

Não executa movimentação de dinheiro

Responsabilidades:

Orquestrar o fluxo de pagamento

Gerar o transaction_uuid

Coordenar limites, registro da transação e execução na carteira

🔹 Serviço de Limites

Dono das regras de limite (diário / mensal)

Valida se um pagamento é permitido

Não executa pagamentos

Não orquestra outros serviços

Princípio-chave:

Limites validam decisões, não executam ações.

Modelo de resposta:

HTTP 200 quando a avaliação ocorre corretamente

A decisão de negócio vem no corpo da resposta

{
  "allowed": true
}


ou

{
  "allowed": false,
  "reason": "DAILY_LIMIT_EXCEEDED"
}

🔹 Serviço de Transações

Dono do ciclo de vida da transação

Registra transações como PENDING

Atualiza o status com base em eventos

Não executa operações de carteira

Princípio-chave:

Transações representam intenção e resultado, não execução.

🔹 Serviço de Wallet (Domínio Financeiro Central)

Fonte única da verdade para movimentação de dinheiro

Executa débito e crédito

Garante atomicidade entre débito e crédito

Emite eventos que representam fatos já ocorridos

Princípio-chave:

Quem move o dinheiro é dono da verdade.

🔹 Statements / Read Models

Consomem eventos

Constroem visões otimizadas para leitura

Não participam de decisões de negócio

Fluxo de Requisição → Evento

O sistema segue um fluxo explícito e previsível:

Cliente
 → Serviço de Pagamento
   → Serviço de Limites (validação síncrona)
   → Serviço de Transações (registro PENDING)
   → Serviço de Wallet (execução débito/crédito)
     → Eventos emitidos
       → Transações atualizam status
       → Limites atualizam uso
       → Statements atualizam visões

Por que Algumas Chamadas São Síncronas

Chamadas HTTP síncronas são usadas apenas quando uma decisão imediata é necessária, como:

validação de limites

registro da intenção da transação

Isso evita o uso de eventos para decisões que exigem resposta imediata.

Eventos são usados para comunicar fatos, não para fazer perguntas.

Eventos como Fatos

Eventos são emitidos somente após execução e persistência bem-sucedidas.

Exemplo:

{
  "type": "WalletDebited",
  "wallet_id": "b1e7...",
  "transaction_uuid": "9f32...",
  "amount": 100
}


Esses eventos representam fatos consumados, não comandos.

Os consumidores reagem de forma independente.

Atomicidade e Consistência

Operações de carteira são executadas dentro de uma transação de banco de dados, garantindo que:

débito e crédito ocorram juntos

nenhum estado parcial seja persistido

eventos só sejam emitidos após commit

Ou toda a operação é bem-sucedida, ou nada acontece.

Filosofia de Tratamento de Erros

Exceções representam falhas inesperadas ou estados inválidos

O fluxo normal não depende de exceções

Decisões de negócio são explícitas

A camada de API traduz exceções em respostas HTTP

Exceções não são controle de fluxo.
Eventos não são comandos.

Decisões de Design e Trade-offs

Este projeto simplifica intencionalmente alguns aspectos para manter o foco na arquitetura:

Não há broker de mensagens real (Kafka é representado conceitualmente)

Não há retry automático ou idempotência completa

Não há outbox pattern

Não há orquestração distribuída via saga

Esses trade-offs são conscientes e documentados.

Em um sistema de produção, esses pontos seriam tratados com infraestrutura adicional.

Por que Este Projeto é um Showcase

Este repositório tem como objetivo demonstrar:

raciocínio arquitetural em nível sênior

compreensão de sistemas distribuídos

uso correto de comunicação síncrona vs assíncrona

limites claros de domínio

princípios de consistência financeira

Ele não foi projetado para ser implantado diretamente em produção.

Principais Aprendizados

Orquestração pertence à camada de aplicação

Movimentação financeira deve ser atômica

Eventos representam fatos, não intenções

Domínios não devem orquestrar outros domínios

Fluxos explícitos são melhores que acoplamentos implícitos

Nota Final

Este projeto prioriza clareza de design em vez de completude de infraestrutura.
Cada simplificação foi feita de forma intencional e está documentada.


(eng)
💳 Wallet – Distributed Wallet System (Architectural Showcase)
Overview

This project is an architectural showcase designed to demonstrate senior-level system design thinking applied to a financial domain.

The goal is not to provide a production-ready wallet system, but to illustrate how a distributed, event-driven architecture can be designed to handle:

wallet balance movements

transaction lifecycle

limit validation

eventual consistency

domain isolation

The focus is on clear boundaries, orchestration, and flow, rather than infrastructure complexity.

Problem Context

A fintech needs to provide a digital wallet that supports:

balance debit and credit

daily and monthly limits

transaction tracking

consistency across multiple services

scalability and decoupling

This problem is intentionally modeled as multiple independent services, each owning a specific part of the domain.

Architectural Goals

Clear separation of responsibilities

Domain-driven boundaries

Explicit orchestration

Event-based state synchronization

No hidden coupling via shared databases

Explicit handling of success vs failure

Services and Responsibilities
🔹 Payment Service (Orchestrator)

Entry point for payment requests

Coordinates the flow

Calls other services synchronously when an immediate decision is required

Does not execute money movement

Responsibilities:

Orchestrate the payment flow

Generate a transaction_uuid

Coordinate limits, transaction registration, and wallet execution

🔹 Limits Service

Owns wallet limits (daily / monthly)

Validates whether a payment is allowed

Does not execute payments

Does not orchestrate other services

Key principle:

Limits validate decisions, they do not execute actions.

Response model:

HTTP 200 when evaluation succeeds

Business decision returned in the response body

{
  "allowed": true
}


or

{
  "allowed": false,
  "reason": "DAILY_LIMIT_EXCEEDED"
}

🔹 Transaction Service

Owns the transaction lifecycle

Registers transactions as PENDING

Updates transaction status based on events

Does not execute wallet operations

Key principle:

Transactions represent intent and outcome, not execution.

🔹 Wallet Service (Core Financial Domain)

Single source of truth for money movement

Executes debit and credit

Guarantees atomicity between debit and credit

Emits events representing facts that already happened

Key principle:

Whoever moves the money owns the truth.

🔹 Statements / Read Models

Consume events

Build optimized read views

Do not participate in decision-making

Request → Event Flow

The system follows a clear and explicit flow:

Client
 → Payment Service
   → Limits Service (sync validation)
   → Transaction Service (register PENDING)
   → Wallet Service (execute debit/credit)
     → Events emitted
       → Transaction Service updates status
       → Limits Service updates usage
       → Statements update read models

Why Some Calls Are Synchronous

Synchronous HTTP calls are used only when an immediate decision is required, such as:

limit validation

registering transaction intent

This avoids using events for decisions that require an immediate answer.

Events are used to announce facts, not to ask questions.

Events as Facts

Events are emitted only after successful execution and persistence.

Example:

{
  "type": "WalletDebited",
  "wallet_id": "b1e7...",
  "transaction_uuid": "9f32...",
  "amount": 100
}


These events represent facts, not commands.

Consumers react independently.

Atomicity and Consistency

Wallet operations are executed inside a database transaction to guarantee:

debit and credit happen together

no partial state is persisted

events are only emitted after commit

Either the whole operation succeeds, or nothing happens.

Error Handling Philosophy

Exceptions represent unexpected or invalid execution

Normal control flow does not rely on exceptions

Business decisions are explicit in responses

Views translate exceptions into HTTP responses

Exceptions are not control flow.
Events are not commands.

Design Decisions and Trade-offs

This project intentionally simplifies some aspects to keep the focus on architecture:

No real message broker (Kafka is conceptually represented)

No retry or idempotency mechanisms

No outbox pattern

No distributed saga orchestration

These trade-offs are conscious and documented.

In a production system, these concerns would be addressed with additional infrastructure.

Why This Is a Showcase Project

This repository is intended to demonstrate:

senior-level architectural reasoning

understanding of distributed systems

correct use of synchronous vs asynchronous communication

clear domain boundaries

financial consistency principles

It is not intended to be deployed as-is.

Key Takeaways

Orchestration belongs to the application layer

Money movement must be atomic

Events represent facts, not intentions

Domains should not orchestrate each other

Explicit flow is better than implicit coupling

Final Note

This project prioritizes clarity of design over completeness of infrastructure.
Every simplification is intentional and documented.