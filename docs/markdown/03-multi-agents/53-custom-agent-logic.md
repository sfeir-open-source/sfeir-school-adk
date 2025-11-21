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
