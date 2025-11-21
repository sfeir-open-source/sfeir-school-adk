<!-- .slide: class="transition" -->

# Custom Agents

##==##

<!-- .slide -->

# Custom Agent : Concept

<br>

## Au-delà des workflows prédéfinis

<br>

Un **Custom Agent** étend `BaseAgent` et implémente sa propre logique d'orchestration via `_run_async_impl`.

<br>

### Caractéristiques :
- 🎨 **Contrôle total** sur la logique d'exécution
- 🔀 **Logique conditionnelle** personnalisée
- 🧩 **Patterns uniques** non couverts par Sequential/Parallel/Loop
- 🔧 **Intégrations externes** (APIs, DB, etc.)

<br>

> ⚠️ **Concept avancé** : Maîtrisez d'abord LLMAgent et WorkflowAgent

Notes:
Utilisez Custom Agent quand Sequential, Parallel, Loop ne suffisent pas
