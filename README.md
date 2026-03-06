# retailops-agent

Scaffolding inicial em Python para um **Customer Support Agent** com base em Clean Architecture (core/ports/adapters), separação explícita de API, Orchestrator e RAG, e documentação pronta para evolução incremental.

## Visão geral

Este repositório contém apenas a fundação estrutural do projeto:
- API HTTP com FastAPI (`/health`)
- Estrutura de pastas por responsabilidades
- Configuração de ambiente, execução e testes
- Documentação de arquitetura e ADR inicial
- Estrutura de prompts + registry

> Nesta etapa, não há implementação de lógica de negócio/RAG/LLM.

## Arquitetura (componentes)

- `src/retailops/api`: camada de entrada HTTP (FastAPI).
- `src/retailops/core/domain`: entidades e regras de domínio.
- `src/retailops/core/use_cases`: casos de uso da aplicação.
- `src/retailops/core/ports`: interfaces (ports) para dependências externas.
- `src/retailops/orchestrator`: coordenação do agente.
- `src/retailops/rag`: pipeline de recuperação de contexto.
- `src/retailops/adapters`: integrações externas concretas.
- `src/retailops/observability`: configuração de tracing/logging.
- `src/retailops/config`: carregamento/configuração de ambiente.

## Como rodar

1. Instale dependências:

```bash
pip install -e .
pip install -e .[dev]
```

2. Copie variáveis de ambiente:

```bash
cp .env.example .env
```

3. Suba a API:

```bash
make run
```

4. Testes:

```bash
make test
make cov
```

## Como adicionar docs na knowledge_base

Ainda não existe implementação de ingestion/retrieval.
Para preparar a evolução, crie uma pasta `knowledge_base/` na raiz e adicione arquivos `.md` com conteúdo versionado em git. A integração dessa pasta com o módulo `src/retailops/rag` será feita na próxima iteração.

## Exemplo de request/response

Request:

```bash
curl -X GET http://localhost:8000/health
```

Response:

```json
{"status":"ok"}
```
