<!-- .slide -->

# Agrégation des résultats

<br>

## Gestion des résultats parallèles

<br>

### Points clés :

- ⏱️ **Timing** : Les agents peuvent terminer à des moments différents
- 🔄 **Collecte** : Les résultats sont collectés après que tous les agents aient terminé
- ❌ **Gestion d'erreurs** : Si un agent échoue, les autres continuent
- 📊 **Combinaison** : Les résultats sont disponibles dans `ctx.session.state`

<br>

```python
# Tous les résultats sont disponibles après l'exécution
all_data = {
    "weather": ctx.session.state.get("weather_data"),
    "news": ctx.session.state.get("news_data"),
    "stocks": ctx.session.state.get("stock_data")
}
```

Notes:
Le ParallelAgent attend que tous les sous-agents se terminent avant de continuer
