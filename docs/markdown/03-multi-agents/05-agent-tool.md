<!-- .slide: class="transition" -->

# Agent-as-a-Tool

##==##

<!-- .slide -->

# Agent-as-a-Tool : Concept

## Appeler un agent comme un outil

<br>

Cette fonctionnalité permet d'utiliser les capacités d'autres agents en les **appelant comme des outils**. L'Agent-as-a-Tool permet d'invoquer un autre agent pour effectuer une tâche spécifique.

<br>

### Principe :
Un agent A appelle un agent B comme un outil, récupère sa réponse, et **continue à gérer la conversation**.

Notes:
Conceptuellement similaire à créer une fonction Python qui appelle un autre agent

##==##

<!-- .slide -->

# Sub-Agent vs Agent-as-a-Tool

## Différences clés

<br>

| Aspect | Sub-Agent | Agent-as-a-Tool |
|--------|-----------|-----------------|
| **Contrôle** | Transfert à sous-agent | Parent garde le contrôle |
| **Réponse** | Sous-agent répond | Parent traite le résultat |
| **Interactions** | Sous-agent gère | Parent continue |
| **Relation** | Hiérarchie permanente | Consultation à la demande |

<br>

### Analogie :
- **Sub-Agent** = Employé dans votre équipe
- **Agent-as-a-Tool** = Consultant externe que vous appelez si besoin

Notes:
L'agent-as-a-tool est invoqué dynamiquement par le LLM si nécessaire

##==##

<!-- .slide: class="with-code max-height" -->

# Agent-as-a-Tool : Implémentation

## Code Python

```python
from google.adk.agents import LlmAgent
from google.adk.tools import AgentTool

# Créer un agent spécialisé
calculator_agent = LlmAgent(
    name="Calculator",
    model="gemini-2.5-flash",
    system_instruction="Effectue des calculs mathématiques précis"
)

# Envelopper comme outil
calc_tool = AgentTool(agent=calculator_agent)

# Agent principal avec l'agent-outil
main_agent = LlmAgent(
    name="Assistant",
    model="gemini-2.5-flash",
    system_instruction="Assistant général qui peut utiliser une calculatrice",
    tools=[calc_tool]  # Agent en tant qu'outil
)
```

Notes:
Le LLM de l'assistant décide quand invoquer calc_tool

##==##

<!-- .slide: class="with-code" -->

# Options de personnalisation

## Configuration d'AgentTool

<br>

### `skip_summarization`

```python
tool = AgentTool(
    agent=specialist_agent,
    skip_summarization=True  # Désactive la résumé par LLM
)
```

- **True** : Bypass la résumé, utilise directement la réponse de l'agent
- **False** (défaut) : Le LLM résume la réponse de l'agent-outil

<br>

### Autres options :
- Nom et description personnalisés du tool
- Metadata de configuration

Notes:
skip_summarization est utile quand la réponse de l'agent-outil est déjà bien formatée

##==##

<!-- .slide -->

# Quand utiliser Agent-as-a-Tool ?

## Cas d'usage typiques

<br>

### 🎯 Délégation dynamique basée sur l'input
L'agent principal décide intelligemment quel spécialiste consulter

### 🔧 Capacités spécialisées occasionnelles
Fonctionnalités nécessaires ponctuellement, pas en permanence

### 💬 Maintien du contexte conversationnel
L'agent parent garde le contrôle de la conversation

<br>

### Exemples :
- **Assistant général** avec outils : juridique, médical, technique
- **Agent support client** avec spécialistes : facturation, technique, retours
- **Agent de recherche** avec experts thématiques

Notes:
Le LLM choisit quand et quel outil appeler basé sur le contexte

##==##

<!-- .slide: class="with-code max-height" -->

# Exemple pratique : Support client

## Agent avec spécialistes multiples

```python
# Définition des agents spécialisés
billing_agent = LlmAgent(
    name="BillingSpecialist",
    system_instruction="Expert en facturation et paiements"
)

technical_agent = LlmAgent(
    name="TechnicalSpecialist",
    system_instruction="Expert en support technique"
)

returns_agent = LlmAgent(
    name="ReturnsSpecialist",
    system_instruction="Expert en retours et remboursements"
)

# Agent principal avec les spécialistes comme outils
support_agent = LlmAgent(
    name="CustomerSupport",
    system_instruction="Agent support qui route vers les spécialistes",
    tools=[
        AgentTool(agent=billing_agent),
        AgentTool(agent=technical_agent),
        AgentTool(agent=returns_agent)
    ]
)
```

Notes:
Le support_agent décide automatiquement quel spécialiste consulter
