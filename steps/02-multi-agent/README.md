# Workshop 02 : Assistant de Recherche Multi-Agents

## Description

Dans ce workshop, vous allez construire un **assistant de recherche intelligent** qui utilise plusieurs patterns d'agents ADK pour collecter, analyser et résumer des informations depuis différentes sources.

### Objectifs d'apprentissage

- ✅ Implémenter un **Sequential Agent** pour un pipeline de traitement
- ✅ Utiliser un **Parallel Agent** pour collecter des données simultanément
- ✅ Ajouter un **Loop Agent** pour le raffinement itératif
- ✅ Intégrer un **Agent-as-a-Tool** pour des capacités spécialisées
- ✅ (Bonus) Créer un **Custom Agent** pour un routing intelligent

---

## Comment exécuter ?

### Prérequis

```bash
pip install google-adk
export GOOGLE_API_KEY="votre_clé_api"
```

### Lancer le workshop

```bash
cd ./steps/02-multi-agent
python research_assistant.py
```

---

## 🎯 Partie 1 : Pipeline Séquentiel (20 min)

### Objectif
Créer un pipeline séquentiel : **Requête → Recherche → Extraction → Résumé**

### Instructions

1. Dans `research_assistant.py`, créez trois agents LLM :
   - `query_planner` : Analise la requête utilisateur et crée un plan de recherche
   - `search_agent` : Simule une recherche et retourne des résultats
   - `summarizer` : Résume les informations trouvées

2. Créez un `SequentialAgent` qui orchestre ces trois agents

### Code à compléter

```python
from google.adk.agents import SequentialAgent, LlmAgent

# TODO: Créer query_planner
query_planner = LlmAgent(
    name="QueryPlanner",
    model="gemini-2.0-flash",
    system_instruction="Analise la requête et crée un plan de recherche structuré"
)

# TODO: Créer search_agent
search_agent = # ...

# TODO: Créer summarizer
summarizer = # ...

# TODO: Créer le pipeline séquentiel
research_pipeline = SequentialAgent(
    name="ResearchPipeline",
    sub_agents=[...]  # À compléter
)
```

### Test
Requête : "Quelles sont les tendances en IA pour 2024 ?"

---

## 🎯 Partie 2 : Collecte Parallèle (20 min)

### Objectif
Ajouter un **Parallel Agent** pour interroger plusieurs sources simultanément

### Instructions

1. Créez trois agents qui simulent des sources différentes :
   - `web_source` : Recherche web
   - `academic_source` : Articles académiques
   - `news_source` : Actualités récentes

2. Créez un `ParallelAgent` pour les exécuter simultanément

3. Intégrez ce `ParallelAgent` dans le pipeline séquentiel existant

### Code à compléter

```python
from google.adk.agents import ParallelAgent

# TODO: Créer les agents de sources
web_source = LlmAgent(
    name="WebSource",
    system_instruction="Recherche des informations sur le web"
)

# TODO: Créer les autres sources
academic_source = # ...
news_source = # ...

# TODO: Créer le ParallelAgent
parallel_sources = ParallelAgent(
    name="MultiSourceFetcher",
    sub_agents=[...]  # À compléter
)

# TODO: Intégrer dans le pipeline
# Modifier research_pipeline pour inclure parallel_sources
```

---

## 🎯 Partie 3 : Boucle de Raffinement (15 min)

### Objectif
Utiliser un **Loop Agent** pour améliorer itérativement la qualité du résumé

### Instructions

1. Créez un agent `quality_checker` qui évalue la qualité (1-10)
2. Créez un `LoopAgent` qui :
   - Génère un résumé
   - Vérifie la qualité
   - Si qualité < 8, améliore et recommence
   - Maximum 3 itérations

### Code à compléter

```python
from google.adk.agents import LoopAgent

# TODO: Créer quality_checker
quality_checker = LlmAgent(
    name="QualityChecker",
    system_instruction="""Évalue la qualité du résumé (1-10).
    Critères : clarté, complétude, concision.
    Met 'quality_approved' à True si score >= 8"""
)

# TODO: Créer le LoopAgent
refinement_loop = LoopAgent(
    name="QualityRefinement",
    sub_agents=[summarizer, quality_checker],
    max_iterations=3,
    stop_condition=lambda ctx: ctx.session.state.get("quality_approved", False)
)
```

---

## 🎯 Partie 4 : Agent-as-a-Tool (15 min)

### Objectif
Ajouter un **fact-checker** comme Agent-as-a-Tool

### Instructions

1. Créez un agent `fact_checker` spécialisé dans la vérification de faits
2. Enveloppez-le avec `AgentTool`
3. Ajoutez-le comme outil à l'agent principal

### Code à compléter

```python
from google.adk.tools import AgentTool

# TODO: Créer fact_checker
fact_checker = LlmAgent(
    name="FactChecker",
    model="gemini-2.0-flash",
    system_instruction="Vérifie la précision des affirmations"
)

# TODO: Créer AgentTool
fact_check_tool = AgentTool(agent=fact_checker)

# TODO: Ajouter l'outil à l'agent principal
main_assistant = LlmAgent(
    name="ResearchAssistant",
    tools=[fact_check_tool]
)
```

---

## 🎯 Partie 5 (Bonus) : Custom Agent (20 min)

### Objectif
Créer un **Custom Agent** qui route intelligemment vers différents spécialistes

### Instructions

1. Créez un `SmartRouterAgent` qui étend `BaseAgent`
2. Implémentez `_run_async_impl` pour :
   - Analyser le type de requête (technique, scientifique, générale)
   - Router vers l'agent spécialisé approprié

### Code à compléter

```python
from google.adk.agents import BaseAgent
from google.adk.types import SessionContext

class SmartRouterAgent(BaseAgent):
    def __init__(self, name: str):
        super().__init__(name=name)
        # TODO: Créer les agents spécialisés
        self.tech_agent = LlmAgent(...)
        self.science_agent = LlmAgent(...)
        self.general_agent = LlmAgent(...)
    
    async def _run_async_impl(self, ctx: SessionContext):
        # TODO: Analyser le type de requête
        query = ctx.session.state.get("user_query", "")
        
        # TODO: Router vers le bon agent
        if "code" in query or "programming" in query:
            return await self.tech_agent.run_async(ctx)
        elif "science" in query or "research" in query:
            return await self.science_agent.run_async(ctx)
        else:
            return await self.general_agent.run_async(ctx)
```

---

## 📊 Critères de succès

Votre assistant devrait :

- ✅ Traiter la requête en pipeline séquentiel
- ✅ Collecter des données depuis plusieurs sources en parallèle
- ✅ Raffiner itérativement jusqu'à qualité acceptable
- ✅ Permettre la vérification de faits via un outil
- ✅ (Bonus) Router intelligemment selon le type de requête

---

## 💡 Conseils

- **État partagé** : Utilisez `ctx.session.state` pour partager les données
- **Débogage** : Ajoutez des prints pour suivre le flux d'exécution
- **Itératif** : Commencez simple, testez, puis ajoutez la complexité
- **Documentation** : Consultez [ADK Docs](https://google.github.io/adk-docs/)

---

## 🎓 Ressources

- [Sequential Agents](https://google.github.io/adk-docs/agents/workflow-agents/sequential-agents/)
- [Parallel Agents](https://google.github.io/adk-docs/agents/workflow-agents/parallel-agents/)
- [Loop Agents](https://google.github.io/adk-docs/agents/workflow-agents/loop-agents/)
- [Agent-as-a-Tool](https://google.github.io/adk-docs/tools-custom/function-tools/#agent-tool)
- [Custom Agents](https://google.github.io/adk-docs/agents/custom-agents/)

---

## ✅ Solution

La solution complète se trouve dans `../02-multi-agent-solution/`

Bon courage ! 🚀
