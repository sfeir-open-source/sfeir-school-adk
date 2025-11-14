import { SfeirThemeInitializer } from '../web_modules/sfeir-school-theme/dist/sfeir-school-theme.mjs';

// One method per module
function schoolSlides() {
  return ['00-school/00-TITLE.md', '00-school/speaker-tanguy.md', '00-school/speaker-baptiste.md'];
}

function introSlides() {
  return ['intro/00-TITLE.md', 'intro/01-introduction-agents.md', 'intro/99-lab-workshop-example.md'];
}

function outillageSlides() {
  return ['01-outillage/00-TITLE.md'];
}

function sessionMemoireSlides() {
  return ['02-session-memoire/00-TITLE.md'];
}

function multiAgentsSlides() {
  return ['03-multi-agents/00-TITLE.md'];
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
