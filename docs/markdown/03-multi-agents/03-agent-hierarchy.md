<!-- .slide -->

# Hiérarchie des agents

<br>

## Organisation structurée des agents

<br>

### Deux règles simples :

1. **Parent & Sous-agents** : Un agent parent peut gérer un ou plusieurs sous-agents
2. **Règle du parent unique** : Chaque agent ne peut avoir qu'un seul parent

<br>

```
    RootAgent (CEO)
    ├── Agent A (VP)
    │   ├── Agent A1 (Director)
    │   └── Agent A2 (Director)
    └── Agent B (VP)
        └── Agent B1 (Manager)
```

Notes:
Analogie : Organigramme d'entreprise - ligne de commande et flux de données clairs

##==##

<!-- .slide -->

# Communication entre agents

<br>

## Trois mécanismes principaux

<br>

### 1. **État de session partagé** 📝
État commun accessible par tous les agents de la hiérarchie

### 2. **Délégation pilotée par LLM** 🤖
L'agent parent décide intelligemment quel sous-agent appeler

### 3. **Invocation explicite (AgentTool)** 🔧
Un agent appelle un autre agent comme un outil/fonction

<br>

Notes:
- État partagé : Comme un tableau blanc commun
- Délégation LLM : Routage intelligent basé sur le contexte
- AgentTool : Consultation d'experts à la demande
