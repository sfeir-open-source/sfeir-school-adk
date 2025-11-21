<!-- .slide -->

# Agent-as-a-Tool : Implémentation

<br>

## Code Python

```python
from google.adk.agents import LlmAgent
from google.adk.tools import AgentTool

# Créer un agent spécialisé
calculator_agent = LlmAgent(
    name="Calculator",
    model="gemini-2.0-flash",
    system_instruction="Effectue des calculs mathématiques précis"
)

# Envelopper comme outil
calc_tool = AgentTool(agent=calculator_agent)

# Agent principal avec l'agent-outil
main_agent = LlmAgent(
    name="Assistant",
    model="gemini-2.0-flash",
    system_instruction="Assistant général qui peut utiliser une calculatrice",
    tools=[calc_tool]  # Agent en tant qu'outil
)
```

Notes:
Le LLM de l'assistant décide quand invoquer calc_tool
