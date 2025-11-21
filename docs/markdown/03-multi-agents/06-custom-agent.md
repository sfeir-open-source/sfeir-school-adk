<!-- .slide: class="transition" -->

# Custom Agents

##==##

<!-- .slide -->

# Custom Agent : Concept

<br>

## Au-delà des workflows prédéfinis

<br>

Un **Custom Agent** étend `BaseAgent` et implémente sa propre logique d'orchestration via `_run_async_impl`.

<br>

### Caractéristiques :
- 🎨 **Contrôle total** sur la logique d'exécution
- 🔀 **Logique conditionnelle** personnalisée
- 🧩 **Patterns uniques** non couverts par Sequential/Parallel/Loop
- 🔧 **Intégrations externes** (APIs, DB, etc.)

<br>

> ⚠️ **Concept avancé** : Maîtrisez d'abord LLMAgent et WorkflowAgent

Notes:
Utilisez Custom Agent quand Sequential, Parallel, Loop ne suffisent pas
<!-- .slide -->

# Quand utiliser Custom Agent ?

<br>

## Situations nécessitant un contrôle personnalisé

<br>

### 🔀 **Logique conditionnelle**
Différents chemins selon les conditions runtime

### 📊 **Gestion d'état complexe**
Logique de state management sophistiquée

### 🌐 **Intégrations externes**
Appels APIs, bases de données, bibliothèques custom

### 🎯 **Sélection dynamique d'agents**
Choisir les sous-agents à la volée

### 🔧 **Patterns de workflow uniques**
Orchestrations qui ne rentrent pas dans Sequential/Parallel/Loop

Notes:
Si vous vous demandez "puis-je faire ça avec Sequential/Parallel/Loop ?" et la réponse est non, utilisez Custom Agent
<!-- .slide -->

# Structure d'un Custom Agent

<br>

## Extension de BaseAgent

```python
from google.adk.agents import BaseAgent, LlmAgent
from google.adk.types import SessionContext

class StoryFlowAgent(BaseAgent):
    def __init__(self, name: str):
        super().__init__(name=name)
        
        # Définir les sous-agents
        self.planner = LlmAgent(name="Planner", ...)
        self.writer = LlmAgent(name="Writer", ...)
        self.editor = LlmAgent(name="Editor", ...)
    
    async def _run_async_impl(self, ctx: SessionContext):
        # Logique d'orchestration personnalisée
        
        # 1. Planification
        plan = await self.planner.run_async(ctx)
        
        # 2. Logique conditionnelle
        if ctx.session.state.get("complexity") > 5:
            # Logique multi-chapitres
            ...
        else:
            # Logique simple
            ...
        
        # 3. Édition finale
        return await self.editor.run_async(ctx)
```

Notes:
_run_async_impl est où vous implémentez votre logique custom
<!-- .slide -->

# Implémentation de logique custom

<br>

## Opérations courantes

<br>

### Accéder au contexte et à l'état
```python
async def _run_async_impl(self, ctx: SessionContext):
    # Lire l'état
    user_level = ctx.session.state.get("user_level", "beginner")
    
    # Écrire dans l'état
    ctx.session.state["processed"] = True
```

### Appeler des sous-agents
```python
# Exécution d'un sous-agent
result = await self.sub_agent.run_async(ctx)
```

### Prendre des décisions
```python
# Logique conditionnelle
if condition:
    await self.agent_a.run_async(ctx)
else:
    await self.agent_b.run_async(ctx)
```

Notes:
Vous avez un contrôle total sur quand et comment appeler les sous-agents
<!-- .slide -->

# Gestion de l'état

<br>

## State management dans Custom Agents

<br>

### Lecture de l'état
```python
value = ctx.session.state.get("key")
value_with_default = ctx.session.state.get("key", "default_value")
```

### Écriture dans l'état
```python
ctx.session.state["result"] = computed_value
ctx.session.state["step_completed"] = True
```

### Partage avec sous-agents
```python
# L'état est automatiquement partagé
ctx.session.state["shared_data"] = data
await self.sub_agent.run_async(ctx)  # Peut accéder à shared_data
```

<br>

> 💡 L'état persiste pendant toute la durée de la session

Notes:
Utilisez l'état pour coordonner entre différentes parties de votre logique
<!-- .slide -->

# Exemple pratique : Agent d'apprentissage adaptatif

<br>

## Adaptation dynamique au niveau de l'utilisateur

```python
class AdaptiveTutorAgent(BaseAgent):
    def __init__(self, name: str):
        super().__init__(name=name)
        self.assessor = LlmAgent(name="LevelAssessor", ...)
        self.beginner_tutor = LlmAgent(name="BeginnerTutor", ...)
        self.intermediate_tutor = LlmAgent(name="IntermediateTutor", ...)
        self.advanced_tutor = LlmAgent(name="AdvancedTutor", ...)
    
    async def _run_async_impl(self, ctx: SessionContext):
        # 1. Évaluer le niveau
        await self.assessor.run_async(ctx)
        level = ctx.session.state.get("user_level")
        
        # 2. Router vers le tuteur approprié
        if level == "beginner":
            return await self.beginner_tutor.run_async(ctx)
        elif level == "intermediate":
            return await self.intermediate_tutor.run_async(ctx)
        else:
            return await self.advanced_tutor.run_async(ctx)
```

Notes:
Sélection dynamique du sous-agent basée sur l'évaluation
