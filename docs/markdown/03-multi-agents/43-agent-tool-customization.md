<!-- .slide -->

# Options de personnalisation

<br>

## Configuration d'AgentTool

<br>

### `skip_summarization`

```python
tool = AgentTool(
    agent=specialist_agent,
    skip_summarization=True  # Désactive la résumé par LLM
)
```

- **True** : Bypass la résumé, utilise directement la réponse de l'agent
- **False** (défaut) : Le LLM résume la réponse de l'agent-outil

<br>

### Autres options :
- Nom et description personnalisés du tool
- Metadata de configuration

Notes:
skip_summarization est utile quand la réponse de l'agent-outil est déjà bien formatée
