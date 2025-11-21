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
