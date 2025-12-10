<!-- .slide: class="transition" -->

# Optimisation du Contexte

##==##

<!-- .slide -->

# Le Challenge du Contexte

## Pourquoi optimiser ?

<br>

Dans une conversation longue, l'historique (contexte) s'accumule rapidement.

### Problèmes majeurs :
1. **Coûts Exponentiels** 💸 : Vous repayez pour relire tout l'historique à chaque nouvelle question.
2. **Latence** ⏱️ : Le "Time to First Token" augmente avec la taille du prompt.
3. **Fenetre Limitée** 🪟 : Même avec 1M/2M tokens, on finit par atteindre la limite ou diluer l'attention du modèle ("Lost in the Middle").

<br>

### Solutions ADK :
- **Caching** : Ne pas re-uploader ce qui ne change pas.
- **Compression** : Résumer ce qui est vieux.

Notes:
L'optimisation du contexte est critique pour passer du prototype (chat court) à la production (assistants de longue durée).

##==##

<!-- .slide: class="with-code max-height" -->

# Context Caching

## Réutiliser le contexte statique

Idéal pour les gros documents ou les instructions système complexes qui ne changent pas.

```python
from google.adk import Agent
from google.adk.apps.app import App
from google.adk.agents.context_cache_config import ContextCacheConfig

root_agent = Agent(
  # configure an agent using Gemini 2.5 or higher
)
app = App(
    name='my-caching-agent-app',
    root_agent=root_agent,
    context_cache_config=ContextCacheConfig(
        min_tokens=2048,    # Nombre minimum de tokens pour activer le cache
        ttl_seconds=600,    # Cache valide pendant 10 minutes
        cache_intervals=5,  # Met à jour le cache tous les 5 appels
    ),
)
```

Le modèle charge le contexte une fois, et les appels suivants sont beaucoup plus rapides et moins chers (tarif "cached input").

<!-- .element: class="admonition note" -->

Notes:
Gemini offre du "Context Caching" explicite. ADK le gère pour vous via cette config.

##==##

<!-- .slide: class="with-code max-height" -->

# Context Compression

Pour gérer une conversation "infinie", on ne peut pas tout garder. La compression résume le passé.

## Workflow de Compression

![](./assets/images/context-compaction.png 'context-compaction')

- **Événement 3 terminé** : Les 3 premiers événements sont compressés en un résumé.
- **Événement 6 terminé** : Les événements 3 à 6 sont compressés, avec un chevauchement d'un événement précédent.
- **Événement 9 terminé** : Les événements 6 à 9 sont compressés, avec un chevauchement d'un événement précédent.

Notes:
C'est transparent pour l'utilisateur. Le modèle a "mémoire" des faits anciens via le résumé, mais travaille sur un contexte court.

##==##
<!-- .slide: class="with-code max-height" -->
# Implémentation de la Compression

```python
from google.adk.apps.app import App, EventsCompactionConfig
from google.adk.apps.llm_event_summarizer import LlmEventSummarizer
from google.adk.models import Gemini

# Define the AI model to be used for summarization:
summarization_llm = Gemini(model="gemini-2.5-flash")

# Create the summarizer with the custom model:
my_summarizer = LlmEventSummarizer(llm=summarization_llm)

# Configure the App with the custom summarizer and compaction settings:
app = App(
    name='my-agent',
    root_agent=root_agent,
    events_compaction_config=EventsCompactionConfig(
        compaction_interval=3,
        overlap_size=1,
        summarizer=my_summarizer,
    ),
)
```
