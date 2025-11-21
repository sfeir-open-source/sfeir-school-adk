<!-- .slide -->

# Exemple pratique : Analyse concurrentielle

<br>

## Recherche sur plusieurs concurrents simultanément

<br>

```python
competitor1_agent = LlmAgent(
    name="Competitor1Analyzer",
    system_instruction="Analyse le concurrent 1 : stratégie, prix, produits"
)

competitor2_agent = LlmAgent(
    name="Competitor2Analyzer",
    system_instruction="Analyse le concurrent 2 : stratégie, prix, produits"
)

competitor3_agent = LlmAgent(
    name="Competitor3Analyzer",
    system_instruction="Analyse le concurrent 3 : stratégie, prix, produits"
)

competitive_analysis = ParallelAgent(
    name="CompetitiveAnalysis",
    sub_agents=[competitor1_agent, competitor2_agent, competitor3_agent]
)

# Résultat : rapport complet sur tous les concurrents
```

Notes:
Gain de temps : 3x plus rapide que l'approche séquentielle
