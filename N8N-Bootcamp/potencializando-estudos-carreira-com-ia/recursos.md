# 📚 Curadoria de Recursos e Materiais de Apoio

Guia consolidado de referências, documentações, ferramentas e links organizados por semana e por categoria.

---

## 🛠️ Ferramentas Essenciais do Bootcamp

- **Automação & Orquestração**:
  - [n8n Official Documentation](https://docs.n8n.io/) — Guia completo de nós, triggers e expressões.
  - [n8n AI / LangChain Nodes](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/) — Documentação dos nós de agentes, ferramentas e memória.
  - [n8n Community Templates](https://n8n.io/workflows/) — Milhares de fluxos prontos para importar e estudar.
- **Modelos e APIs de IA**:
  - [Google AI Studio (Gemini API)](https://aistudio.google.com/) — Chaves gratuitas para testes com modelos Gemini 1.5/2.0 Flash e Pro.
  - [OpenAI Platform & Docs](https://platform.openai.com/docs) — Referência de chamadas de API, formatação e functions.
  - [Anthropic Claude Docs](https://docs.anthropic.com/) — Guias sobre Claude 3.5 Sonnet e system prompts.
  - [Groq Cloud](https://console.groq.com/) — Provedor de inferência ultrarrápida com modelos open-source (Llama 3, Mistral).
- **Ambiente & Editores**:
  - [VS Code](https://code.visualstudio.com/) / Antigravity IDE
  - [WSL (Windows Subsystem for Linux)](https://learn.microsoft.com/pt-br/windows/wsl/) — Ambiente Linux de alta performance integrado ao Windows.
  - [Docker Desktop](https://www.docker.com/products/docker-desktop/) — Para rodar instâncias locais do n8n via container.

---

## 📌 Semana 01: Fundamentos de IA & Chatbots Inteligentes

### Documentações & Guias
- [Prompt Engineering Guide (DAIR.AI)](https://www.promptingguide.ai/pt) — Referência mais completa sobre técnicas de prompts em português.
- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering) — Estratégias recomendadas pela OpenAI.
- [Anthropic Prompt Library](https://docs.anthropic.com/en/prompt-library/library) — Exemplos reais de prompts avançados e roles.

### Leituras & Artigos Recomendados
- *Como funcionam os Transformers e LLMs* (Visão intuitiva sem jargões matemáticos complexos).
- *Diferenças práticas entre Zero-Shot, Few-Shot e Chain-of-Thought*.
- *Técnica Feynman para autodidatas em tecnologia*.

### Repositório de Apoio
- [DIO - Potencializando seus Estudos e Carreira com IA](https://github.com/digitalinnovationone/potencializando-estudos-carreira-com-ia) — Repositório base com diretrizes do curso.

---

## 📌 Semana 02: Copilotos & Aceleração no Desenvolvimento

### Ferramentas & Extensões
- [GitHub Copilot Documentation](https://docs.github.com/pt/copilot) — Guia oficial de comandos, chat e configurações.
- [GitHub Copilot Cheat Sheet](https://github.blog/) — Principais atalhos e boas práticas de contexto.

### Melhores Práticas
- *Como fornecer contexto claro para copilotos*: Manter arquivos relevantes abertos, criar boas assinaturas de funções e comentários descritivos.
- *Testes gerados por IA*: Como validar e refinar testes unitários sem confiar cegamente nas respostas.
- *Refatoração segura*: Test-Driven Development (TDD) assistido por IA.

---

## 📌 Semana 03: Automação de Processos com n8n & IA

### Tutoriais e Recursos Práticos
- [n8n Quick Start Guide](https://docs.n8n.io/getting-started/quick-start/) — Passo a passo para criar o primeiro workflow.
- [Trabalhando com Dados JSON no n8n](https://docs.n8n.io/data/data-structure/) — Compreendendo as estruturas `$json`.
- [Construindo seu primeiro AI Agent no n8n](https://docs.n8n.io/advanced-ai/intro/) — Conceitos de Chat Trigger, Model, Memory e Tools.

### Casos de Uso Clássicos para Praticar
1. **Webhook + LLM**: Receber formulário de contato e classificar prioridade com IA.
2. **Resumo Inteligente**: Monitorar feed RSS ou canal e enviar resumo semanal via e-mail ou Discord.
3. **Agente com Tool**: Agente n8n com capacidade de buscar dados meteorológicos ou cotações via API HTTP.

---

## 📌 Semana 04: Projeto Final Integrador, Portfólio & Carreira

### Guias de Apresentação e Portfólio
- [Guia de READMEs Incríveis no GitHub](https://github.com/matiassingers/awesome-readme) — Modelos de documentação que chamam atenção de recrutadores e gestores.
- [Como Documentar Projetos de Automação](https://mermaid.js.org/) — Criação de diagramas visuais e fluxogramas claros.
- [ScreenToGif / OBS Studio](https://www.screentogif.com/) — Ferramentas gratuitas para gravar demonstrações em GIF do workflow funcionando.

### Dicas de Posicionamento no LinkedIn
- Foque na dor do negócio: *Qual problema esse fluxo resolveu? Quanto tempo/custo economizou?*
- Estrutura de post recomendada:
  1. Gancho (O desafio/problema).
  2. Solução adotada (Tecnologias: n8n + LLM + Integrações).
  3. Resultado ou demonstração prática (Vídeo curto ou print do fluxo).
  4. Link para o repositório GitHub com o código e documentação completa.
