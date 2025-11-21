"""
Workshop 02 - Multi-Agent Research Assistant - SOLUTION
SFEIR School ADK

Solution complète du workshop multi-agents
"""

from google.adk.agents import SequentialAgent, ParallelAgent, LoopAgent, LlmAgent, BaseAgent
from google.adk.tools import AgentTool
from google.adk.types import SessionContext


# =============================================================================
# PARTIE 1 : PIPELINE SÉQUENTIEL - SOLUTION
# =============================================================================

def create_sequential_pipeline():
    """Pipeline séquentiel : Plan → Recherche → Résumé"""
    
    query_planner = LlmAgent(
        name="QueryPlanner",
        model="gemini-2.0-flash",
        system_instruction="""Analyse la requête utilisateur et crée un plan de recherche structuré.
        Identifie les thèmes clés et les sources potentielles."""
    )
    
    search_agent = LlmAgent(
        name="SearchAgent",
        model="gemini-2.0-flash",
        system_instruction="""Simule une recherche basée sur le plan.
        Retourne des informations détaillées et pertinentes."""
    )
    
    summarizer = LlmAgent(
        name="Summarizer",
        model="gemini-2.0-flash",
        system_instruction="""Résume les résultats de recherche de manière claire et concise.
        Structure : Introduction, Points clés, Conclusion."""
    )
    
    pipeline = SequentialAgent(
        name="ResearchPipeline",
        sub_agents=[query_planner, search_agent, summarizer]
    )
    
    return pipeline, summarizer


# =============================================================================
# PARTIE 2 : COLLECTE PARALLÈLE - SOLUTION
# =============================================================================

def create_parallel_sources():
    """Sources parallèles : Web + Académique + News"""
    
    web_source = LlmAgent(
        name="WebSource",
        model="gemini-2.0-flash",
        system_instruction="""Simule une recherche web généraliste.
        Fournis des informations à jour et accessibles."""
    )
    
    academic_source = LlmAgent(
        name="AcademicSource",
        model="gemini-2.0-flash",
        system_instruction="""Simule une recherche dans des articles académiques.
        Fournis des informations scientifiques et rigoureuses."""
    )
    
    news_source = LlmAgent(
        name="NewsSource",
        model="gemini-2.0-flash",
        system_instruction="""Simule une recherche dans les actualités récentes.
        Fournis des informations à jour sur les tendances actuelles."""
    )
    
    parallel_fetcher = ParallelAgent(
        name="MultiSourceFetcher",
        sub_agents=[web_source, academic_source, news_source]
    )
    
    return parallel_fetcher


def create_enhanced_pipeline():
    """Pipeline avec collecte parallèle intégrée"""
    
    query_planner = LlmAgent(
        name="QueryPlanner",
        model="gemini-2.0-flash",
        system_instruction="Analyse la requête et crée un plan de recherche"
    )
    
    parallel_sources = create_parallel_sources()
    
    summarizer = LlmAgent(
        name="Summarizer",
        model="gemini-2.0-flash",
        system_instruction="""Résume et synthétise les informations de toutes les sources.
        Crée un résumé cohérent et structuré."""
    )
    
    enhanced_pipeline = SequentialAgent(
        name="EnhancedResearchPipeline",
        sub_agents=[query_planner, parallel_sources, summarizer]
    )
    
    return enhanced_pipeline, summarizer


# =============================================================================
# PARTIE 3 : BOUCLE DE RAFFINEMENT - SOLUTION
# =============================================================================

def create_refinement_loop(summarizer):
    """Boucle de raffinement de qualité"""
    
    quality_checker = LlmAgent(
        name="QualityChecker",
        model="gemini-2.0-flash",
        system_instruction="""Évalue la qualité du résumé sur une échelle de 1 à 10.
        
        Critères d'évaluation :
        - Clarté : Le résumé est-il facile à comprendre ?
        - Complétude : Couvre-t-il tous les points importants ?
        - Concision : Est-il concis sans être trop court ?
        
        Si le score est >= 8, mets 'quality_approved' à True dans l'état.
        Sinon, suggère des améliorations spécifiques."""
    )
    
    refinement_loop = LoopAgent(
        name="QualityRefinement",
        sub_agents=[summarizer, quality_checker],
        max_iterations=3,
        stop_condition=lambda ctx: ctx.session.state.get("quality_approved", False)
    )
    
    return refinement_loop


# =============================================================================
# PARTIE 4 : AGENT-AS-A-TOOL - SOLUTION
# =============================================================================

def create_fact_checker_tool():
    """Fact-checker comme AgentTool"""
    
    fact_checker = LlmAgent(
        name="FactChecker",
        model="gemini-2.0-flash",
        system_instruction="""Expert en vérification de faits.
        
        Analyse les affirmations et vérifie leur exactitude.
        Identifie les potentielles inexactitudes ou exagérations.
        Fournis des corrections si nécessaire."""
    )
    
    fact_check_tool = AgentTool(
        agent=fact_checker,
        skip_summarization=False
    )
    
    return fact_check_tool


def create_main_assistant_with_tools():
    """Assistant principal avec fact-checker comme outil"""
    
    fact_check_tool = create_fact_checker_tool()
    
    main_assistant = LlmAgent(
        name="ResearchAssistant",
        model="gemini-2.0-flash",
        system_instruction="""Assistant de recherche intelligent.
        
        Tu peux utiliser le fact-checker pour vérifier l'exactitude des informations.
        Utilise-le quand tu as des doutes sur des affirmations importantes.""",
        tools=[fact_check_tool]
    )
    
    return main_assistant


# =============================================================================
# PARTIE 5 (BONUS) : CUSTOM AGENT - SOLUTION
# =============================================================================

class SmartRouterAgent(BaseAgent):
    """Custom Agent qui route intelligemment vers des spécialistes"""
    
    def __init__(self, name: str):
        super().__init__(name=name)
        
        self.tech_agent = LlmAgent(
            name="TechSpecialist",
            model="gemini-2.0-flash",
            system_instruction="""Expert en technologie et programmation.
            Fournis des informations techniques précises et à jour."""
        )
        
        self.science_agent = LlmAgent(
            name="ScienceSpecialist",
            model="gemini-2.0-flash",
            system_instruction="""Expert en sciences et recherche académique.
            Fournis des informations scientifiques rigoureuses."""
        )
        
        self.general_agent = LlmAgent(
            name="GeneralSpecialist",
            model="gemini-2.0-flash",
            system_instruction="""Expert généraliste.
            Fournis des informations complètes et accessibles."""
        )
    
    async def _run_async_impl(self, ctx: SessionContext):
        """Route vers le spécialiste approprié basé sur la requête"""
        
        query = ctx.session.state.get("user_query", "").lower()
        
        # Mots-clés pour le routing
        tech_keywords = ["code", "programming", "software", "algorithm", "api", "tech"]
        science_keywords = ["science", "research", "study", "academic", "paper"]
        
        # Logique de routing
        if any(keyword in query for keyword in tech_keywords):
            ctx.session.state["routed_to"] = "TechSpecialist"
            return await self.tech_agent.run_async(ctx)
        elif any(keyword in query for keyword in science_keywords):
            ctx.session.state["routed_to"] = "ScienceSpecialist"
            return await self.science_agent.run_async(ctx)
        else:
            ctx.session.state["routed_to"] = "GeneralSpecialist"
            return await self.general_agent.run_async(ctx)


# =============================================================================
# FONCTION PRINCIPALE - SOLUTION
# =============================================================================

async def main():
    """Test de toutes les implémentations"""
    
    print("=" * 70)
    print("Workshop 02 - Multi-Agent Research Assistant - SOLUTION")
    print("=" * 70)
    
    test_query = "Quelles sont les tendances en IA pour 2024 ?"
    print(f"\n📝 Requête : {test_query}\n")
    
    # Partie 1: Sequential Pipeline
    print("\n" + "=" * 70)
    print("PARTIE 1 : Sequential Pipeline")
    print("=" * 70)
    pipeline, _ = create_sequential_pipeline()
    print(f"✅ Sequential Pipeline créé avec {len(pipeline.sub_agents)} agents")
    print(f"   Agents : {[agent.name for agent in pipeline.sub_agents]}")
    
    # Partie 2: Parallel Sources
    print("\n" + "=" * 70)
    print("PARTIE 2 : Parallel Sources")
    print("=" * 70)
    parallel = create_parallel_sources()
    print(f"✅ Parallel Agent créé avec {len(parallel.sub_agents)} sources")
    print(f"   Sources : {[agent.name for agent in parallel.sub_agents]}")
    
    enhanced_pipeline, summarizer = create_enhanced_pipeline()
    print(f"✅ Enhanced Pipeline avec collecte parallèle créé")
    
    # Partie 3: Refinement Loop
    print("\n" + "=" * 70)
    print("PARTIE 3 : Refinement Loop")
    print("=" * 70)
    refinement = create_refinement_loop(summarizer)
    print(f"✅ Refinement Loop créé")
    print(f"   Max iterations : {refinement.max_iterations}")
    print(f"   Sub-agents : {[agent.name for agent in refinement.sub_agents]}")
    
    # Partie 4: Agent-as-a-Tool
    print("\n" + "=" * 70)
    print("PARTIE 4 : Agent-as-a-Tool")
    print("=" * 70)
    fact_tool = create_fact_checker_tool()
    assistant = create_main_assistant_with_tools()
    print(f"✅ Fact-checker tool créé")
    print(f"✅ Assistant principal avec {len(assistant.tools)} outil(s)")
    
    # Partie 5: Custom Agent (Bonus)
    print("\n" + "=" * 70)
    print("PARTIE 5 (BONUS) : Custom Router Agent")
    print("=" * 70)
    router = SmartRouterAgent(name="SmartRouter")
    print(f"✅ Smart Router créé")
    print(f"   Spécialistes : TechSpecialist, ScienceSpecialist, GeneralSpecialist")
    
    # Test du routing
    test_queries = [
        "Comment programmer en Python ?",
        "Quelles sont les dernières découvertes en physique quantique ?",
        "Quelles sont les tendances en IA ?"
    ]
    
    print("\n   Tests de routing :")
    for test_q in test_queries:
        query_lower = test_q.lower()
        if any(k in query_lower for k in ["code", "programming", "python"]):
            expected = "TechSpecialist"
        elif any(k in query_lower for k in ["science", "physique"]):
            expected = "ScienceSpecialist"
        else:
            expected = "GeneralSpecialist"
        print(f"   - \"{test_q}\" → {expected}")
    
    print("\n" + "=" * 70)
    print("✅ Tous les composants ont été créés avec succès !")
    print("=" * 70)
    
    print("\n💡 Pour tester en production, décommentez les appels .run() dans le code")


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
