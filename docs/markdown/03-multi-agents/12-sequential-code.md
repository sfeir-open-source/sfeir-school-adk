<!-- .slide -->

# Sequential Agent : Implémentation

<br>

## Code Python

```python
from google.adk.agents import SequentialAgent, LlmAgent

# Définir les sous-agents
step1 = LlmAgent(
    name="DataFetcher",
    model="gemini-2.0-flash",
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
