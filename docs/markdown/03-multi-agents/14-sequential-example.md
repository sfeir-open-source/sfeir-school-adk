<!-- .slide -->

# Exemple pratique : Création d'article de blog

<br>

## Pipeline de génération de contenu

<br>

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
