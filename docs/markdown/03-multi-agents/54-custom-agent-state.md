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
