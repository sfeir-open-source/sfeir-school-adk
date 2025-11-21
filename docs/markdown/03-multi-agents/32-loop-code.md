<!-- .slide -->

# Loop Agent : Implémentation

<br>

## Code Python

```python
from google.adk.agents import LoopAgent, LlmAgent

# Définir les agents pour la boucle
generator = LlmAgent(
    name="CodeGenerator",
    system_instruction="Génère du code Python"
)

validator = LlmAgent(
    name="CodeValidator",
    system_instruction="Valide la qualité du code et suggère améliorations"
)

# Créer la boucle avec condition d'arrêt
refinement_loop = LoopAgent(
    name="CodeRefinementLoop",
    sub_agents=[generator, validator],
    max_iterations=5,
    stop_condition=lambda ctx: ctx.session.state.get("validation_passed")
)
```

Notes:
La boucle s'arrête quand validation_passed est True OU après 5 itérations max
