# 📅 Cronograma Semanal de Estudos (Semanas 1 a 4)

> Utilize as caixas de seleção (`- [ ]`) para marcar as tarefas concluídas à medida que avança.

---

## 🗓️ Semana 01: Fundamentos de IA & Chatbots Inteligentes

**Meta da semana**: Compreender os fundamentos das LLMs, dominar padrões de prompt engineering e construir um tutor de estudos personalizado.

- [ ] **Dia 1: Panorama da IA Generativa & Ecossistema de Modelos**
  - [ ] Compreender o funcionamento básico de modelos de linguagem (tokens, contexto, temperatura).
  - [ ] Explorar as diferenças entre os principais modelos: GPT-4o, Claude 3.5 Sonnet e Gemini Flash/Pro.
  - [ ] Configurar ambiente de trabalho e organizar pastas de anotações.
- [ ] **Dia 2: Engenharia de Prompts na Prática (Nível Básico a Intermediário)**
  - [ ] Padrões de prompt: *Zero-shot*, *Few-shot* e *Role Prompting*.
  - [ ] Delimitação de contexto, formatos de saída (JSON, Markdown, Tabelas) e restrições negativas.
  - [ ] Exercício: Criar 3 prompts para tarefas diárias (resumir artigo, gerar perguntas de revisão, traduzir código).
- [ ] **Dia 3: Técnicas Avançadas de Raciocínio (Chain-of-Thought & Decomposição)**
  - [ ] Aplicar técnicas de *Chain-of-Thought* (Passo a passo) para resolver problemas lógicos complexos.
  - [ ] Decomposição de tarefas em sub-etapas guiadas por IA.
  - [ ] Comparar respostas dos modelos para o mesmo desafio de raciocínio.
- [ ] **Dia 4: IA como Aceleradora de Aprendizado**
  - [ ] Utilizar chatbots com a Técnica Feynman (pedir para a IA avaliar sua explicação).
  - [ ] Geração de flashcards, quizzes simulados e mapas mentais em texto a partir de temas técnicos.
- [ ] **Dia 5: Projeto da Semana — Tutor Pessoal Customizado**
  - [ ] Desenvolver um *System Prompt* / Instrução Customizada para um tutor especializado em n8n e IA.
  - [ ] Testar cenários reais com o tutor e salvar o prompt em `anotacoes/semana-01.md`.
- [ ] **Fim de Semana: Revisão e Retrospectiva**
  - [ ] Preencher a retrospectiva semanal em `anotacoes/semana-01.md`.
  - [ ] Duplicar o modelo para a semana seguinte (`anotacoes/semana-02.md`).

---

## 🗓️ Semana 02: Copilotos & Aceleração de Desenvolvimento

**Meta da semana**: Integrar copilotos de IA ao dia a dia de código e automação, multiplicando a velocidade de escrita, teste e documentação.

- [ ] **Dia 1: Configuração e Fluxo com Copilotos de Código**
  - [ ] Configuração do GitHub Copilot ou assistente inline no editor (VS Code / Antigravity).
  - [ ] Atalhos essenciais: autocompletar, inline edit e comandos de chat lateral.
  - [ ] Compreender o conceito de contexto ativo (arquivos abertos, comentários e guias de projeto).
- [ ] **Dia 2: Geração de Código Assistida & Prototipagem Rápida**
  - [ ] Usar comentários descritivos como gatilhos para geração de funções e scripts (JavaScript/Python).
  - [ ] Geração de scripts utilitários para tratamento de dados e conversão de formatos.
- [ ] **Dia 3: Geração de Testes Unitários e Validação**
  - [ ] Gerar testes unitários para funções existentes com apoio do copiloto.
  - [ ] Explorar casos de borda (edge cases) sugeridos pela IA.
- [ ] **Dia 4: Refatoração, Detecção de Falhas e Segurança**
  - [ ] Identificar pontos de melhoria, gargalos de performance e vulnerabilidades comuns.
  - [ ] Refatorar código legado mantendo a legibilidade e boas práticas.
- [ ] **Dia 5: Mini-Projeto — Script Utilitário Completo**
  - [ ] Criar do zero um script com documentação, testes e tratamento de erros construído 100% em parceria com o Copilot.
  - [ ] Registrar lições aprendidas e prompts mais eficazes no diário de bordo.
- [ ] **Fim de Semana: Retrospectiva da Semana 2**
  - [ ] Preencher `anotacoes/semana-02.md` e preparar ambiente para o n8n.

---

## 🗓️ Semana 03: Automação de Processos & Agentes com n8n

**Meta da semana**: Dominar os conceitos fundamentais do n8n e integrar nós de IA para construir agentes inteligentes capazes de executar tarefas dinâmicas.

- [ ] **Dia 1: Fundamentos do n8n (Arquitetura e Conceitos)**
  - [ ] Instalar/acessar o n8n (Docker local ou n8n Cloud).
  - [ ] Entender a estrutura: Workflows, Triggers (Gatilhos), Nodes, Execuções e Webhooks.
  - [ ] Criar o primeiro fluxo básico: Webhook de entrada -> Manipulação de dados -> Resposta HTTP.
- [ ] **Dia 2: Manipulação de Dados no n8n**
  - [ ] Estrutura de dados JSON no n8n (`$json`, `$binary`, `$item`).
  - [ ] Utilizar o *Code Node* (JavaScript/Python) para transformações e filtros customizados.
  - [ ] Tratamento de arrays e paginação de dados.
- [ ] **Dia 3: Integração de APIs de LLM no n8n**
  - [ ] Configuração de credenciais de APIs (OpenAI, Gemini, Groq ou Anthropic).
  - [ ] Uso do nó de LLM simples para processar textos, resumir conteúdos e extrair entidades estruturadas.
- [ ] **Dia 4: Construção de Agentes Inteligentes no n8n (AI Agent Node)**
  - [ ] Conceitos de agentes no n8n: Modelos, Memória (Window Buffer / Motor de Memória) e Ferramentas (*Tools*).
  - [ ] Conectar uma ferramenta ao agente (ex: busca na web, consulta a calculadora ou HTTP Request).
  - [ ] Testar decisões autônomas do agente a partir de perguntas variadas.
- [ ] **Dia 5: Mini-Projeto da Semana — Fluxo Inteligente com IA**
  - [ ] Construir um fluxo prático no n8n (ex: Agente que recebe mensagem via Webhook/Telegram/Discord, consulta uma fonte e retorna resposta personalizada).
  - [ ] Exportar o JSON do workflow e salvar no repositório.
- [ ] **Fim de Semana: Retrospectiva da Semana 3**
  - [ ] Documentar o fluxo criado em `anotacoes/semana-03.md`.

---

## 🗓️ Semana 04: Projeto Prático Integrador, Portfólio & Carreira

**Meta da semana**: Consolidar todo o conhecimento em um projeto final de impacto, documentá-lo de forma profissional e posicionar seu aprendizado no mercado.

- [ ] **Dia 1: Concepção e Escopo do Projeto Final**
  - [ ] Definir o problema real a ser resolvido pelo fluxo n8n com IA (ex: Triagem de leads, assistente de suporte inteligente, gerador automatizado de relatórios).
  - [ ] Desenhar a arquitetura do fluxo (diagrama de blocos / nós).
- [ ] **Dia 2: Desenvolvimento do Workflow Principal**
  - [ ] Montagem dos nós de integração, chamadas de IA e rotas condicionais (If/Switch).
  - [ ] Implementação de tratamento de erros (*Error Trigger* e mensagens de fallback).
- [ ] **Dia 3: Testes de Ponta a Ponta & Otimização**
  - [ ] Execução de testes com múltiplos cenários e tipos de dados de entrada.
  - [ ] Otimização do consumo de tokens (ajuste de prompts de sistema e escolha correta do modelo).
- [ ] **Dia 4: Documentação Completa do Projeto**
  - [ ] Criação de um README dedicado com: descrição do problema, solução, diagrama do fluxo, variáveis necessárias e guia de execução.
  - [ ] Gravação de um GIF ou vídeo curto demonstrando o workflow em ação.
- [ ] **Dia 5: Posicionamento Estratégico & Portfólio**
  - [ ] Publicar o código/workflow no GitHub com documentação impecável.
  - [ ] Elaborar uma publicação no LinkedIn compartilhando a solução, lições aprendidas e o impacto da automação com IA.
- [ ] **Fim de Semana: Autoavaliação e Plano Pós-Bootcamp**
  - [ ] Preencher a autoavaliação final em `anotacoes/semana-04.md`.
  - [ ] Definir as próximas metas de especialização contínua.
