<!-- .slide -->

# Gestion de l'état séquentiel

<br>

## Passage de données entre agents

<br>

### Utilisation de `ctx.session.state`

```python
# Agent 1 : Écrit dans l'état
ctx.session.state["raw_data"] = data

# Agent 2 : Lit l'état
raw_data = ctx.session.state.get("raw_data")
cleaned_data = clean(raw_data)
ctx.session.state["cleaned_data"] = cleaned_data

# Agent 3 : Utilise les résultats précédents
results = analyze(ctx.session.state.get("cleaned_data"))
```

<br>

> L'état est **partagé** entre tous les agents de la hiérarchie

Notes:
Comme un tableau blanc partagé que chaque agent peut lire et modifier
