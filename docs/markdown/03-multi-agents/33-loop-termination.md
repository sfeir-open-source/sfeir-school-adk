<!-- .slide -->

# Conditions d'arrêt

<br>

## Stratégies de terminaison de boucle

<br>

### 1. **Nombre maximum d'itérations**
```python
max_iterations=10  # Arrêt après 10 tours max
```

### 2. **Condition basée sur l'état**
```python
stop_condition=lambda ctx: ctx.session.state.get("quality_score") > 8
```

### 3. **Condition de succès/échec**
```python
stop_condition=lambda ctx: ctx.session.state.get("task_completed") == True
```

<br>

> ⚠️ **Important** : Toujours définir `max_iterations` pour éviter les boucles infinies

Notes:
Combinez plusieurs conditions pour plus de contrôle
