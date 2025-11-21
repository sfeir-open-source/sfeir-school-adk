<!-- .slide: class="transition" -->

# Sequential Agent

##==##

<!-- .slide -->

# Sequential Agent : Vue d'ensemble

<br>

## Le pattern de la chaîne d'assemblage

<br>

Un **Sequential Agent** exécute ses sous-agents **un après l'autre**, dans un ordre prédéfini.

<br>

```
Agent 1 ➜ Agent 2 ➜ Agent 3 ➜ Agent 4
```

<br>

### Caractéristiques :
- ✅ Flux déterministe et prévisible
- ✅ La sortie d'un agent peut devenir l'entrée du suivant
- ✅ Idéal pour les pipelines multi-étapes

Notes:
Comme une chaîne de production : chaque étape doit être complétée avant la suivante
