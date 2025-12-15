<!-- .slide: class="transition" -->

# Structured Output

##==##

<!-- .slide -->

# Structured Output : Vue d'ensemble

## Pourquoi structurer les échanges ?

Les LLMs génèrent naturellement du texte non structuré. Pour les intégrer dans des systèmes logiciels, nous avons besoin de **garanties** sur le format des entrées et sorties.

<br>

### 3 Mécanismes Clés :

1. **Input Schema** 📥 : Valide ce qui entre dans l'agent
2. **Output Schema** 📤 : Force le format de ce qui sort (JSON)
3. **Output Key** 🔑 : Sauvegarde automatiquement le résultat dans le state

Sans structure, le parsing des réponses est fragile et sujet aux erreurs. Ces outils rendent les agents déterministes dans leur format.
<!-- .element: class="admonition tip" -->

##==##

<!-- .slide: class="with-code max-height" -->

# Input Schema

## Valider les entrées utilisateur

Définit la structure attendue pour les messages envoyés à l'agent.

```python
from google.adk.agents import LlmAgent
from pydantic import BaseModel, Field

# Définition du schéma d'entrée
class UserQuery(BaseModel):
    city: str = Field(description="La ville cible")
    days: int = Field(description="Durée du séjour", ge=1)

# Configuration de l'agent
travel_agent = LlmAgent(
    name="TravelGuide",
    model="gemini-2.5-flash",
    input_schema=UserQuery,  # Validation automatique
    system_instruction="Crée un itinéraire de voyage."
)
```

En utilisant Pydantic pour la validation, si l'entrée ne correspond pas au schéma, une erreur est levée avant même d'appeler le modèle.

<!-- .element: class="admonition note" -->

##==##

<!-- .slide: class="with-code max-height" -->

# Output Schema

## Forcer une réponse structurée (JSON)

Garantit que l'agent répondra toujours avec un objet JSON valide conforme à votre modèle.

```python
class TripPlan(BaseModel):
    destination: str
    activities: list[str]
    estimated_cost: float

planner = LlmAgent(
    name="Planner",
    model="gemini-2.5-flash",
    output_schema=TripPlan, # Force le JSON strict
    system_instruction="Génère un plan de voyage structuré."
)

# Utilisation
response = await planner.run_async("Paris pour 3 jours")
# response.text sera un JSON valide :
# {"destination": "Paris", "activities": [...], "estimated_cost": 500.0}
```

Indispensable pour que d'autres systèmes (API, Frontend, Base de données) puissent consommer la réponse de l'agent sans parsing complexe.

<!-- .element: class="admonition tip" -->

##==##

<!-- .slide: class="with-code" -->

# Output Key

## Partage de données multi-agents

Sauvegarde automatiquement la réponse dans le `SessionState` pour les agents suivants.

```python
researcher = LlmAgent(
    name="Researcher",
    # ...
    output_key="research_data"  # Sauvegarde dans state["research_data"]
)
writer = LlmAgent(
    name="Writer",
    # ...
    # Pas besoin de passer explicitement les données,
    # le writer a accès au state global
    system_instruction="Utilise les données de recherche pour rédiger un article: {research_data}."
)
# Évite d'avoir à gérer manuellement le flux de données dans le code d'orchestration.
sequential_agent = SequentialAgent(
    name="ResearchAndWrite",
    agents=[researcher, writer]
)
```

Dans un SequentialAgent, c'est le moyen le plus propre de passer le "baton" de données d'un agent à l'autre.

<!-- .element: class="admonition tip" -->
