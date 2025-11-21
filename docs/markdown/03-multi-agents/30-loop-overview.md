<!-- .slide: class="transition" -->

# Loop Agent

##==##

<!-- .slide -->

# Loop Agent : Vue d'ensemble

<br>

## Exécution itérative avec condition

<br>

Un **Loop Agent** exécute **répétitivement** ses sous-agents jusqu'à ce qu'une condition soit remplie.

<br>

```
┌──────────────────┐
│  Exécute agents  │
└────────┬─────────┘
         │
    Condition ? ────── Non ──┐
         │                   │
        Oui                  │
         │                   │
     Termine  ←──────────────┘
```

<br>

### Caractéristiques :
- 🔄 Comme une boucle `while` en programmation
- ⏹️ Conditions d'arrêt configurables
- 🛡️ Limite maximale d'itérations

Notes:
Utile pour le raffinement itératif et les tentatives avec retry
