<!-- .slide -->

# Exemple pratique : Raffinement de contenu

<br>

## Amélioration itérative jusqu'à qualité acceptable

<br>

```python
content_generator = LlmAgent(
    name="ContentGenerator",
    system_instruction="Génère du contenu marketing"
)

quality_checker = LlmAgent(
    name="QualityChecker",
    system_instruction="""Évalue la qualité (1-10) sur:
    - Clarté, Engagement, SEO
    - Met 'quality_passed' à True si score >= 8"""
)

content_refinement = LoopAgent(
    name="ContentRefinement",
    sub_agents=[content_generator, quality_checker],
    max_iterations=5,
    stop_condition=lambda ctx: ctx.session.state.get("quality_passed")
)

# Résultat : Contenu de haute qualité ou 5 tentatives
```

Notes:
La boucle continue jusqu'à obtenir un contenu de qualité >= 8 ou 5 essais max
