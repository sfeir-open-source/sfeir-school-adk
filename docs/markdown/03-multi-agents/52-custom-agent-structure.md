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
