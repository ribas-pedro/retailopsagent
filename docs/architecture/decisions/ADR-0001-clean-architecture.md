# ADR-0001: Adoção de Clean Architecture

- **Status:** Aceita
- **Data:** 2026-03-05

## Contexto
O projeto precisa escalar em complexidade (novos providers LLM, evolução de RAG, múltiplas interfaces de entrada) sem perda de testabilidade.

## Decisão
Adotar Clean Architecture com separação entre:
- core (domínio, use cases, ports)
- adapters (integrações)
- camadas de borda (API, orchestrator, rag, observability/config)

## Trade-offs
- **Prós:** baixo acoplamento, facilidade de testes, evolução segura.
- **Contras:** mais arquivos desde o início e boilerplate inicial.
