<!-- .slide: class="transition" -->

# Sequential Agent

##==##

<!-- .slide -->

# Sequential Agent : Vue d'ensemble

## Le pattern de la chaîne d'assemblage

<br>

Un **Sequential Agent** exécute ses sous-agents **un après l'autre**, dans un ordre prédéfini.

<br>

```
Agent 1 ➜ Agent 2 ➜ Agent 3 ➜ Agent 4
```

<br>

### Caractéristiques :
- ✅ Flux déterministe et prévisible
- ✅ La sortie d'un agent peut devenir l'entrée du suivant
- ✅ Idéal pour les pipelines multi-étapes

Notes:
Comme une chaîne de production : chaque étape doit être complétée avant la suivante

##==##

<!-- .slide -->

# Quand utiliser Sequential Agent ?

## Cas d'usage typiques

<br>

### 📊 Pipelines de données
```
Récupération ➜ Nettoyage ➜ Analyse ➜ Résumé
```

### 📝 Traitement de documents
```
Chargement ➜ Extraction ➜ Traduction ➜ Formatage
```

### 🎨 Création de contenu
```
Recherche ➜ Plan ➜ Rédaction ➜ Révision
```

<br>

Utilisez Sequential Agent quand les étapes **dépendent les unes des autres**

<!-- .element: class="admonition important" -->

Notes:
Chaque étape nécessite les résultats de l'étape précédente

##==##

<!-- .slide: class="with-code max-height" -->

# Sequential Agent : Implémentation

## Code Python

```python
from google.adk.agents import SequentialAgent, LlmAgent

# Définir les sous-agents
step1 = LlmAgent(
    name="DataFetcher",
    model="gemini-2.5-flash",
    system_instruction="Récupère des données depuis les sources"
)

step2 = LlmAgent(name="DataCleaner", ...)
step3 = LlmAgent(name="DataAnalyzer", ...)

# Créer le workflow séquentiel
pipeline = SequentialAgent(
    name="DataPipeline",
    sub_agents=[step1, step2, step3]
)
```

Notes:
Les agents s'exécutent dans l'ordre du tableau : step1 → step2 → step3

##==##

<!-- .slide: class="with-code" -->

# Gestion de l'état séquentiel

## Passage de données entre agents

<br>

### Utilisation de `ctx.session.state`

```python
# Agent 1 : Écrit dans l'état
ctx.session.state["raw_data"] = data

# Agent 2 : Lit l'état
raw_data = ctx.session.state.get("raw_data")
cleaned_data = clean(raw_data)
ctx.session.state["cleaned_data"] = cleaned_data

# Agent 3 : Utilise les résultats précédents
results = analyze(ctx.session.state.get("cleaned_data"))
```

<br>

L'état est **partagé** entre tous les agents de la hiérarchie

<!-- .element: class="admonition tip" -->

Notes:
Comme un tableau blanc partagé que chaque agent peut lire et modifier

##==##

<!-- .slide: class="with-code max-height" -->

# Exemple pratique : Création d'article de blog

## Pipeline de génération de contenu

```python
research_agent = LlmAgent(
    name="Researcher",
    system_instruction="Recherche des informations sur le sujet"
)

outline_agent = LlmAgent(
    name="Outliner", 
    system_instruction="Crée un plan structuré"
)

writer_agent = LlmAgent(
    name="Writer",
    system_instruction="Rédige le contenu complet"
)

reviewer_agent = LlmAgent(
    name="Reviewer",
    system_instruction="Révise et améliore la qualité"
)

blog_pipeline = SequentialAgent(
    name="BlogCreator",
    sub_agents=[research_agent, outline_agent, writer_agent, reviewer_agent]
)
```

Notes:
Chaque étape améliore progressivement le résultat final
