import { SfeirThemeInitializer } from '../web_modules/sfeir-school-theme/dist/sfeir-school-theme.mjs';

// One method per module
function schoolSlides() {
  return ['00-school/00-TITLE.md', '00-school/speaker-tanguy.md', '00-school/speaker-baptiste.md'];
}

function introSlides() {
  return ['intro/00-TITLE.md', 'intro/99-lab-workshop-example.md'];
}

function outillageSlides() {
  return ['01-outillage/00-TITLE.md'];
}

function sessionMemoireSlides() {
  return ['02-session-memoire/00-TITLE.md'];
}

function multiAgentsSlides() {
  return [
    '03-multi-agents/00-TITLE.md',
    '03-multi-agents/01-intro-multi-agents.md',
    '03-multi-agents/02-adk-agent-types.md',
    '03-multi-agents/03-agent-hierarchy.md',
    '03-multi-agents/10-sequential-overview.md',
    '03-multi-agents/11-sequential-use-cases.md',
    '03-multi-agents/12-sequential-code.md',
    '03-multi-agents/13-sequential-state.md',
    '03-multi-agents/14-sequential-example.md',
    '03-multi-agents/20-parallel-overview.md',
    '03-multi-agents/21-parallel-use-cases.md',
    '03-multi-agents/22-parallel-code.md',
    '03-multi-agents/23-parallel-results.md',
    '03-multi-agents/24-parallel-example.md',
    '03-multi-agents/30-loop-overview.md',
    '03-multi-agents/31-loop-use-cases.md',
    '03-multi-agents/32-loop-code.md',
    '03-multi-agents/33-loop-termination.md',
    '03-multi-agents/34-loop-example.md',
    '03-multi-agents/40-agent-tool-overview.md',
    '03-multi-agents/41-agent-tool-comparison.md',
    '03-multi-agents/42-agent-tool-code.md',
    '03-multi-agents/43-agent-tool-customization.md',
    '03-multi-agents/44-agent-tool-use-cases.md',
    '03-multi-agents/45-agent-tool-example.md',
    '03-multi-agents/50-custom-agent-overview.md',
    '03-multi-agents/51-custom-agent-use-cases.md',
    '03-multi-agents/52-custom-agent-structure.md',
    '03-multi-agents/53-custom-agent-logic.md',
    '03-multi-agents/54-custom-agent-state.md',
    '03-multi-agents/55-custom-agent-example.md',
    '03-multi-agents/60-a2a-protocol.md',
    '03-multi-agents/61-a2a-benefits.md',
    '03-multi-agents/99-lab-multi-agent.md',
  ];
}

function fonctionnalitesAvanceesSlides() {
  return ['04-fonctionnalites-avancees/00-TITLE.md'];
}

export function formation() {
  return [
    //
    ...schoolSlides(),
    ...introSlides(),
    ...outillageSlides(),
    ...sessionMemoireSlides(),
    ...multiAgentsSlides(),
    ...fonctionnalitesAvanceesSlides(),
  ].map((slidePath) => {
    return { path: slidePath };
  });
}

SfeirThemeInitializer.init(formation);
