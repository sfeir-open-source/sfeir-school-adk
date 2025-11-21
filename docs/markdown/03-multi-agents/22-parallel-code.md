<!-- .slide -->

# Parallel Agent : Implémentation

<br>

## Code Python

```python
from google.adk.agents import ParallelAgent, LlmAgent

# Définir des sous-agents indépendants
weather_agent = LlmAgent(
    name="WeatherAPI",
    system_instruction="Récupère les données météo"
)

news_agent = LlmAgent(
    name="NewsAPI",
    system_instruction="Récupère les actualités"
)

stock_agent = LlmAgent(
    name="StockAPI",
    system_instruction="Récupère les données boursières"
)

# Créer le workflow parallèle
parallel_fetcher = ParallelAgent(
    name="MultiSourceFetcher",
    sub_agents=[weather_agent, news_agent, stock_agent]
)
```

Notes:
Les trois agents s'exécutent simultanément, pas d'ordre garanti
