<!-- .slide -->

# Exemple pratique : Support client

<br>

## Agent avec spécialistes multiples

<br>

```python
# Créer les agents spécialisés
billing_agent = LlmAgent(
    name="BillingSpecialist",
    system_instruction="Expert en facturation et paiements"
)

technical_agent = LlmAgent(
    name="TechnicalSpecialist",
    system_instruction="Expert en support technique"
)

returns_agent = LlmAgent(
    name="ReturnsSpecialist",
    system_instruction="Expert en retours et remboursements"
)

# Agent principal avec les spécialistes comme outils
support_agent = LlmAgent(
    name="CustomerSupport",
    system_instruction="Agent support qui route vers les spécialistes",
    tools=[
        AgentTool(agent=billing_agent),
        AgentTool(agent=technical_agent),
        AgentTool(agent=returns_agent)
    ]
)
```

Notes:
Le support_agent décide automatiquement quel spécialiste consulter
