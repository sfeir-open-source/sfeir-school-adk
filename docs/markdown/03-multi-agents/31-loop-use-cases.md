<!-- .slide -->

# Quand utiliser Loop Agent ?

<br>

## Cas d'usage typiques

<br>

### 🔄 Mécanismes de retry
```
Tenter API call → Si échec, réessayer avec backoff
```

### 📈 Raffinement itératif
```
Générer → Évaluer → Si qualité insuffisante, améliorer
```

### 📊 Polling d'API
```
Vérifier statut → Si non terminé, attendre et réessayer
```

### 🎯 Amélioration progressive
```
Code → Tests → Si tests échouent, corriger le code
```

<br>

> **Règle d'or** : Utilisez Loop Agent pour les tâches qui nécessitent **plusieurs tentatives** ou **amélioration progressive**

Notes:
Toujours définir une condition d'arrêt pour éviter les boucles infinies
