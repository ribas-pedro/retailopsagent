# 01 - Components

## Componentes e responsabilidades

### API (`src/retailops/api`)
- Expor endpoints HTTP
- Validar contratos de entrada/saída
- Delegar para casos de uso/orquestrador

### Core Domain (`src/retailops/core/domain`)
- Entidades
- Value objects
- Regras de negócio puras

### Use Cases (`src/retailops/core/use_cases`)
- Fluxos da aplicação
- Coordenação de regras de domínio

### Ports (`src/retailops/core/ports`)
- Interfaces para LLM, storage, telemetry, etc.

### Orchestrator (`src/retailops/orchestrator`)
- Coordenação de agente
- Estratégias de execução

### RAG (`src/retailops/rag`)
- Indexação/recuperação
- Construção de contexto para resposta

### Adapters (`src/retailops/adapters`)
- Implementações concretas de providers e infra

### Observability (`src/retailops/observability`)
- Configuração de tracing/logging

### Config (`src/retailops/config`)
- Leitura e validação de variáveis de ambiente
