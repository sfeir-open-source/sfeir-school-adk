# Solution - Workshop 02 : Assistant de Recherche Multi-Agents

## Vue d'ensemble

Cette solution implémente un assistant de recherche intelligent utilisant tous les patterns multi-agents ADK.

## Structure de la solution

### Partie 1 : Sequential Pipeline ✅

```python
Pipeline : QueryPlanner → SearchAgent → Summarizer
```

**Agents créés :**
- `QueryPlanner` : Analyse et planifie la recherche
- `SearchAgent` : Effectue la recherche simulée
- `Summarizer` : Résume les résultats

### Partie 2 : Parallel Sources ✅

```python
Sources parallèles : WebSource + AcademicSource + NewsSource
```

**Amélioration :**
- Collecte simultanée depuis 3 sources
- Intégration dans le pipeline séquentiel
- Gain de performance (3x plus rapide)

### Partie 3 : Refinement Loop ✅

```python
Loop : Summarizer → QualityChecker (jusqu'à qualité >= 8)
```

**Fonctionnement :**
- Évaluation de qualité sur 3 critères
- Max 3 itérations
- Arrêt quand `quality_approved = True`

### Partie 4 : Agent-as-a-Tool ✅

```python
Agent principal + FactChecker (comme outil)
```

**Caractéristiques :**
- Fact-checker invoqué dynamiquement par le LLM
- Vérification d'exactitude à la demande
- Parent garde le contrôle de la conversation

### Partie 5 : Custom Router Agent ✅ (Bonus)

```python
SmartRouter : Analyse requête → Route vers spécialiste
```

**Spécialistes :**
- `TechSpecialist` : Questions techniques/programmation
- `ScienceSpecialist` : Questions scientifiques/académiques
- `GeneralSpecialist` : Questions générales

**Logique de routing :**
- Mots-clés techniques → TechSpecialist
- Mots-clés scientifiques → ScienceSpecialist
- Autres → GeneralSpecialist

## Exécution de la solution

```bash
cd steps/02-multi-agent-solution
python research_assistant.py
```

### Sortie attendue

```
=================================================================
Workshop 02 - Multi-Agent Research Assistant - SOLUTION
==================================================================

📝 Requête : Quelles sont les tendances en IA pour 2024 ?

==================================================================
PARTIE 1 : Sequential Pipeline
==================================================================
✅ Sequential Pipeline créé avec 3 agents
   Agents : ['QueryPlanner', 'SearchAgent', 'Summarizer']

==================================================================
PARTIE 2 : Parallel Sources
==================================================================
✅ Parallel Agent créé avec 3 sources
   Sources : ['WebSource', 'AcademicSource', 'NewsSource']
✅ Enhanced Pipeline avec collecte parallèle créé

==================================================================
PARTIE 3 : Refinement Loop
==================================================================
✅ Refinement Loop créé
   Max iterations : 3
   Sub-agents : ['Summarizer', 'QualityChecker']

==================================================================
PARTIE 4 : Agent-as-a-Tool
==================================================================
✅ Fact-checker tool créé
✅ Assistant principal avec 1 outil(s)

==================================================================
PARTIE 5 (BONUS) : Custom Router Agent
==================================================================
✅ Smart Router créé
   Spécialistes : TechSpecialist, ScienceSpecialist, GeneralSpecialist

   Tests de routing :
   - "Comment programmer en Python ?" → TechSpecialist
   - "Quelles sont les dernières découvertes en physique quantique ?" → ScienceSpecialist
   - "Quelles sont les tendances en IA ?" → GeneralSpecialist

==================================================================
✅ Tous les composants ont été créés avec succès !
==================================================================
```

## Points clés de l'implémentation

### 1. État partagé (`ctx.session.state`)

```python
# Écriture
ctx.session.state["quality_approved"] = True
ctx.session.state["routed_to"] = "TechSpecialist"

# Lecture
quality = ctx.session.state.get("quality_approved", False)
```

### 2. Conditions d'arrêt (LoopAgent)

```python
stop_condition=lambda ctx: ctx.session.state.get("quality_approved", False)
```

### 3. Agent-as-a-Tool

```python
agent_tool = AgentTool(agent=fact_checker, skip_summarization=False)
main_agent = LlmAgent(..., tools=[agent_tool])
```

### 4. Custom Agent

```python
class SmartRouterAgent(BaseAgent):
    async def _run_async_impl(self, ctx: SessionContext):
        # Logique custom de routing
        if condition:
            return await self.specialist.run_async(ctx)
```

## Concepts démontrés

- ✅ **Composition d'agents** : Pipeline avec Parallel intégré
- ✅ **Orchestration déterministe** : Sequential et Parallel
- ✅ **Exécution itérative** : Loop avec condition
- ✅ **Délégation dynamique** : Agent-as-a-Tool
- ✅ **Logique personnalisée** : Custom Agent avec routing

## Extensions possibles

1. **Ajouter de vraies API** (recherche web, académique)
2. **Implémenter le caching** pour éviter les recherches redondantes
3. **Ajouter la persistance** des résultats dans une base de données
4. **Créer une interface web** avec Streamlit ou Gradio
5. **Monitoring et métriques** de performance des agents

## Ressources

- [Documentation ADK](https://google.github.io/adk-docs/)
- [Guide Multi-Agent](https://cloud.google.com/blog/topics/developers-practitioners/building-collaborative-ai-a-developers-guide-to-multi-agent-systems-with-adk)
- [Exemples ADK](https://github.com/cuppibla/adk_tutorial)
