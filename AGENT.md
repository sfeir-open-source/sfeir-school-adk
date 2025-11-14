# GEMINI Project Context: SFEIR School ADK

This document provides a comprehensive overview of the SFEIR School ADK project, its structure, and the plan for its development. Its purpose is to serve as a guide for the Gemini CLI to assist in the development of this course.

## 1. Project Overview

This project is a SFEIR School course focused on teaching how to create agents with the **ADK (Agent Development Kit) framework in Python**.

The project is based on a generic SFEIR School template and will be adapted for the specific needs of the ADK course.

The project is divided into two main parts:

*   **`docs/`**: A `reveal.js`-based presentation that serves as the course's slides. The content is written in Markdown.
*   **`steps/`**: A series of hands-on labs to practice the concepts learned in the course. The labs will be Python-based.

## 2. Plan for Adaptation to ADK Sfeir School

The following steps will be taken to adapt the generic template for the ADK Sfeir School:

### 2.1. Update Presentation Content

The presentation content in `docs/markdown/` will be updated to reflect the ADK course. This will involve:

1.  **Creating new markdown files** for each chapter of the course. The structure will be based on the `docs/scripts/slides.js` file.
2.  **Updating `docs/scripts/slides.js`** to reference the new markdown files.
3.  **Replacing the generic content** with ADK-specific content, including code examples in Python.

### 2.2. Update Labs

The labs in the `steps/` directory will be replaced with Python-based labs for ADK. This will involve:

1.  **Creating new lab directories** for each lab.
2.  **Creating Python scripts** for the labs.
3.  **Adding a `requirements.txt` file** to each lab directory to specify Python dependencies.
4.  **Updating the `README.md`** in each lab directory with instructions on how to run the lab and the exercises.
5.  **Updating `steps/labs.json`** to reference the new lab directories.

### 2.3. Update Configuration

The following configuration files will be updated:

*   **`README.md`**: The main `README.md` will be updated to reflect the ADK Sfeir School course.
*   **`docs/index.html`**: The title and other metadata will be updated.
*   **`docs/package.json`**: The project name and description will be updated.

## 3. Building and Running

### 3.1. Presentation

To run the presentation locally:

1.  Navigate to the `docs/` directory.
2.  Run `npm install` to install the dependencies.
3.  Run `npm start` to start the local development server.
4.  Open `http://localhost:4242/` in your browser.

### 3.2. Labs

To run the labs:

1.  Navigate to the specific lab directory in `steps/`.
2.  Create a virtual environment: `python3 -m venv .venv && source .venv/bin/activate`
3.  Install the dependencies: `pip install -r requirements.txt`.
4.  Follow the instructions in the lab's `README.md` to run the lab.

## 4. Development Conventions

*   **Code Style**: Python code should follow the PEP 8 style guide.
*   **Commits**: Commit messages should follow the Conventional Commits specification.
*   **Branches**: Create a new branch for each new feature or bug fix.
*   **Pull Requests**: All changes should be submitted via pull requests.
