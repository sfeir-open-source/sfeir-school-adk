<!-- .slide: class="transition" -->

# Best Practices & Patterns Avancés

##==##

<!-- .slide: class="with-code" -->

# Principe du moindre privilège

```python
# ❌ MAUVAIS : Tout donner à l'agent
agent = client.agents.create(
    model='gemini-2.5-flash',
    tools=[
        all_database_tools,
        all_admin_tools,
        all_user_management_tools
    ]
)

# ✅ BON : Outils spécifiques au contexte
agent = client.agents.create(
    model='gemini-2.5-flash',
    tools=[
        read_orders_tool,      # Lecture seulement
        search_products_tool    # Recherche
    ]
    # PAS d'outils d'écriture ou d'admin
)
```

Beaucoup d'outils = Plus de risques et plus de difficultés pour choisir le bon outil

<!-- .element: class="admonition warning" -->

Notes:
- L'agent peut mal choisir un outil
- Risque de side-effects non intentionnels
- Plus difficile à déboguer
- Performances dégradées (trop de choix)
- Principe de sécurité fondamental

##==##

<!-- .slide: class="with-code max-height" -->

# Séparation lecture/écriture
```python
# Outils en lecture seule
read_tools = [
    get_user_info_tool,
    list_products_tool
]
# Outils avec effets de bord
write_tools = [
    create_order_tool,
    delete_product_tool
]
# Agent en lecture seule par défaut
assistant_agent = client.agents.create(
    instructions="Assistant client - consultation uniquement",
    tools=read_tools
)
# Agent admin avec tous les privilèges
admin_agent = client.agents.create(
    instructions="Agent admin - gestion complète",
    tools=read_tools + write_tools,
    # + mécanismes de confirmation pour actions critiques
)
```

Notes:
- Séparer clairement read vs write
- La plupart des agents n'ont besoin que de read
- Write tools = risque plus élevé
- Implémenter des confirmations pour actions critiques
- Audit et logging renforcés sur write operations

##==##

<!-- .slide: class="with-code max-height" -->

# Validation et sanitization

```python
def update_user_email(user_id: str, new_email: str) -> dict:
    """Met à jour l'email d'un utilisateur."""
    
    # 1. Validation des entrées
    if not user_id or not user_id.isdigit():
        return {"error": "user_id invalide"}
    
    # 2. Validation du format email
    import re
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_pattern, new_email):
        return {"error": "Format email invalide"}
    
    # 3. Sanitization (protection injection)
    user_id = int(user_id)  # Conversion sécurisée
    new_email = new_email.strip().lower()
    
    # 4. Vérification des permissions
    if not has_permission(user_id, "update_email"):
        return {"error": "Permission refusée"}

    except Exception as e:
        log_error(e)
        return {"error": "Erreur lors de la mise à jour"}
```

Notes:
- Toujours valider les inputs de l'agent
- Ne jamais faire confiance aveuglément
- Protection contre injection SQL/XSS
- Vérifier les permissions
- Logger les erreurs pour audit
- Retourner des erreurs explicites mais pas trop verbeux

##==##

<!-- .slide: class="with-code max-height" -->

# Observabilité : Logging et tracing

```python
def get_user_info(user_id: str) -> dict:
    """Récupère les infos utilisateur avec logging complet."""
    start_time = datetime.now()
    logger.info(f"Tool call: get_user_info", extra={"tool_name": "get_user_info",
        "user_id": user_id, "timestamp": start_time.isoformat()
    })
    
    try:
        result = database.query(f"SELECT * FROM users WHERE id = {user_id}")
        duration = (datetime.now() - start_time).total_seconds()
        logger.info(f"Tool success: get_user_info", extra={"tool_name": "get_user_info",
            "user_id": user_id, "duration_ms": duration * 1000, "result_size": len(result)
        })
        return result
        
    except Exception as e:
        duration = (datetime.now() - start_time).total_seconds()
        logger.error(f"Tool error: get_user_info", extra={"tool_name": "get_user_info",
            "user_id": user_id, "error": str(e),
            "duration_ms": duration * 1000
        })
        return {"error": "Erreur interne"}
```

Notes:
- Logger tous les appels de tools
- Inclure : timestamp, paramètres, durée, résultat/erreur
- Utiliser structured logging (JSON)
- Intégrer avec Cloud Logging, Datadog, etc.
- Essentiel pour debugging et monitoring
- Analyser les patterns d'usage des tools

##==##

<!-- .slide: class="with-code max-height" -->

# Pattern : Tool chaining

```python
# L'agent peut enchaîner automatiquement
agent_instructions = """
Tu es un assistant de recherche. Quand tu cherches des informations :

1. D'abord, utilise search_web pour trouver des sources
2. Puis, utilise extract_content pour récupérer le contenu
3. Ensuite, utilise analyze_content pour analyser
4. Enfin, utilise generate_summary pour synthétiser

Enchaîne ces outils dans cet ordre pour fournir une réponse complète.
"""
# Les tools
tools = [
    search_web_tool,       # 1. Recherche
    extract_content_tool,  # 2. Extraction
    analyze_content_tool,  # 3. Analyse
    generate_summary_tool  # 4. Synthèse
]
agent = client.agents.create(
    model='gemini-2.5-flash',
    instructions=agent_instructions,
    tools=tools
)
```

Notes:
- Le LLM peut apprendre à enchaîner des tools
- Guider via les instructions système
- Pattern pipeline : output d'un tool → input du suivant
- L'agent peut ajuster le workflow selon le contexte
- Alternative : créer un orchestrateur explicite

##==##

<!-- .slide: class="with-code" -->

# Pattern : Conditional tool selection

```python
agent_instructions = """
Tu disposes de plusieurs outils de recherche. Choisis selon le contexte :

- search_internal_docs : Pour des questions sur nos produits/process internes
- search_web : Pour des informations publiques et actualités
- query_database : Pour des données chiffrées sur nos clients/produits
- ask_expert : Pour des questions complexes nécessitant expertise humaine

Règles de sélection :
1. Toujours commencer par search_internal_docs si lié à l'entreprise
2. Utiliser query_database pour métriques, stats, KPIs
3. search_web seulement pour infos externes non disponibles en interne
4. ask_expert en dernier recours si incertitude forte

Explique quel outil tu utilises et pourquoi.
"""
```

<br>

### Le LLM apprend à choisir l'outil optimal

Notes:
- Guider la sélection via instructions claires
- Hiérarchie de préférence
- Expliquer les critères de choix
- Le LLM peut apprendre des patterns
- Réduire les coûts en priorisant outils moins chers
- Améliorer qualité en choisissant la meilleure source

##==##

<!-- .slide -->

# Récapitulatif : Tooling ADK

**Ce que nous avons vu :**

1. ✅ **Concepts** : Pourquoi les tools sont essentiels
2. ✅ **Gemini Tools** : Google Search, Code Execution
3. ✅ **Google Cloud** : BigQuery, Spanner, Vertex AI, GKE...
4. ✅ **Third-party** : GitHub, Notion, Tavily, Exa...
5. ✅ **Custom Tools** : Function, OpenAPI, MCP
6. ✅ **Best Practices** : Sécurité, observabilité

Vous êtes maintenant prêts à créer des agents puissants ! 🚀

Notes:
- Couverture complète de l'écosystème tooling
- Du plus simple au plus avancé
- Concepts applicables au-delà d'ADK
- La pratique viendra avec les labs
- N'hésitez pas à expérimenter
