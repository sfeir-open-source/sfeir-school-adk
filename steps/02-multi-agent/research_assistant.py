"""
Workshop 02 - Multi-Agent Research Assistant
SFEIR School ADK

À COMPLÉTER : Créez un assistant de recherche utilisant différents patterns multi-agents
"""

from google.adk.agents import SequentialAgent, ParallelAgent, LoopAgent, LlmAgent, BaseAgent
from google.adk.tools import AgentTool
from google.adk.types import SessionContext


# =============================================================================
# PARTIE 1 : PIPELINE SÉQUENTIEL
# =============================================================================

def create_sequential_pipeline():
    """
    TODO: Créer un pipeline séquentiel avec 3 agents :
    1. query_planner : Analyse la requête et crée un plan
    2. search_agent : Effectue la recherche
    3. summarizer : Résume les résultats
    """
    
    # TODO: Créer query_planner
    query_planner = LlmAgent(
        name="QueryPlanner",
        model="gemini-2.0-flash",
        system_instruction="Analyse la requête utilisateur et crée un plan de recherche structuré"
    )
    
    # TODO: Créer search_agent
    search_agent = None  # À COMPLÉTER
    
    # TODO: Créer summarizer
    summarizer = None  # À COMPLÉTER
    
    # TODO: Créer le SequentialAgent
    pipeline = None  # À COMPLÉTER
    
    return pipeline


# =============================================================================
# PARTIE 2 : COLLECTE PARALLÈLE
# =============================================================================

def create_parallel_sources():
    """
    TODO: Créer un ParallelAgent avec 3 sources :
    1. web_source : Recherche web
    2. academic_source : Articles académiques
    3. news_source : Actualités
    """
    
    # TODO: Créer les agents de sources
    web_source = None  # À COMPLÉTER
    academic_source = None  # À COMPLÉTER
    news_source = None  # À COMPLÉTER
    
    # TODO: Créer le ParallelAgent
    parallel_fetcher = None  # À COMPLÉTER
    
    return parallel_fetcher


# =============================================================================
# PARTIE 3 : BOUCLE DE RAFFINEMENT
# =============================================================================

def create_refinement_loop(summarizer):
    """
    TODO: Créer un LoopAgent pour raffiner le résumé
    - Evaluer la qualité (1-10)
    - Boucle jusqu'à qualité >= 8
    - Max 3 itérations
    """
    
    # TODO: Créer quality_checker
    quality_checker = None  # À COMPLÉTER
    
    # TODO: Créer le LoopAgent
    refinement_loop = None  # À COMPLÉTER
    
    return refinement_loop


# =============================================================================
# PARTIE 4 : AGENT-AS-A-TOOL
# =============================================================================

def create_fact_checker_tool():
    """
    TODO: Créer un fact-checker comme AgentTool
    """
    
    # TODO: Créer l'agent fact_checker
    fact_checker = None  # À COMPLÉTER
    
    # TODO: Envelopper comme AgentTool
    fact_check_tool = None  # À COMPLÉTER
    
    return fact_check_tool


def create_main_assistant_with_tools():
    """
    TODO: Créer l'assistant principal avec le fact-checker comme outil
    """
    
    fact_check_tool = create_fact_checker_tool()
    
    # TODO: Créer l'assistant principal avec tools
    main_assistant = None  # À COMPLÉTER
    
    return main_assistant


# =============================================================================
# PARTIE 5 (BONUS) : CUSTOM AGENT
# =============================================================================

class SmartRouterAgent(BaseAgent):
    """
    TODO: Implémenter un Custom Agent qui route vers différents spécialistes
    basé sur le type de requête
    """
    
    def __init__(self, name: str):
        super().__init__(name=name)
        
        # TODO: Créer les agents spécialisés
        self.tech_agent = None  # À COMPLÉTER
        self.science_agent = None  # À COMPLÉTER
        self.general_agent = None  # À COMPLÉTER
    
    async def _run_async_impl(self, ctx: SessionContext):
        """
        TODO: Implémenter la logique de routing
        - Analyser la requête
        - Router vers l'agent approprié
        """
        
        # TODO: Récupérer la requête de l'état
        query = ctx.session.state.get("user_query", "").lower()
        
        # TODO: Implémenter la logique de routing
        # if "keyword" in query:
        #     return await self.tech_agent.run_async(ctx)
        # ...
        
        pass  # À COMPLÉTER


# =============================================================================
# FONCTION PRINCIPALE
# =============================================================================

async def main():
    """
    Fonction principale pour tester votre assistant
    """
    
    print("=" * 60)
    print("Workshop 02 - Multi-Agent Research Assistant")
    print("=" * 60)
    
    # Test de la requête
    test_query = "Quelles sont les tendances en IA pour 2024 ?"
    
    print(f"\n📝 Requête : {test_query}\n")
    
    # TODO: Testez vos implémentations ici
    # Décommentez au fur et à mesure de votre progression
    
    # # Partie 1: Sequential
    # pipeline = create_sequential_pipeline()
    # if pipeline:
    #     result = await pipeline.run(test_query)
    #     print(f"✅ Résultat Sequential: {result}\n")
    
    # # Partie 2: Parallel
    # parallel = create_parallel_sources()
    # if parallel:
    #     result = await parallel.run(test_query)
    #     print(f"✅ Résultat Parallel: {result}\n")
    
    # # Partie 3: Loop
    # # ... etc
    
    print("\n" + "=" * 60)
    print("Fin du workshop")
    print("=" * 60)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
