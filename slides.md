---
marp: true
title: Product Documentation Presentation
theme: custom-tech
paginate: true
_paginate: true
footer: "© 2025 Software Documentation | Contact: 23f2000764@ds.study.iitm.ac.in"
math: katex
---

<!--
custom theme
Save as inline theme so this file is portable in version control
-->
<style>
/* ============================
   Custom Marp Theme: custom-tech
   ============================ */
@import "https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap";

section {
  font-family: "Inter", sans-serif;
  background-color: #f7f9fc;
  color: #1e1e1e;
  padding: 40px;
}

h1, h2, h3 {
  font-weight: 600;
  color: #0d47a1;
}

footer {
  font-size: 12px;
  color: #444;
}

strong {
  color: #0d47a1;
}
</style>

# 🧩 Product Documentation  
### Using Marp for Maintainable, Versioned Docs  
**Author:** 23f2000764@ds.study.iitm.ac.in

---

## Why Marp for Documentation?

- Markdown-based → easy to version control  
- Export formats: **PDF, HTML, PPTX**  
- Developer-friendly workflow  
- Lightweight and automatable in CI/CD  
- Custom themes for consistent branding

---

## Features of Our Documentation Workflow

- Single source of truth (`.md`)
- Custom theming  
- Automated builds with Marp CLI  
- Embed:
  - Code blocks  
  - Diagrams  
  - Math equations  
  - Rich styling

---

<!-- background image slide -->
<!-- Use any public URL or local relative image -->
---
marp: true
backgroundImage: url("https://cdn-front.freepik.com/images/ai/image-generator/cover/image-generator-header.webp?w=3840&h=1920&q=90%203840w,%20https://cdn-front.freepik.com/images/ai/image-generator/cover/image-generator-header.webp?w=7680&h=3840&q=90%207680w")
backgroundSize: cover
class: lead
---

# 🌐 Visual Overview  
## Background Image Example Slide

This slide demonstrates using **background images** with Marp directives.

---

## Algorithmic Complexity Example

The complexity of our indexing algorithm:

\[
T(n) = O(n \log n)
\]

Space complexity:

\[
S(n) = O(n)
\]

Graph traversal runtime:

\[
T_{\text{bfs}} = O(V + E)
\]

---

## Custom-Styled Callout

<div style="padding: 15px; border-left: 6px solid #0d47a1; background:#e3f2fd;">
  <strong>Note:</strong> All documentation is auto-generated nightly from our Markdown repository.
</div>

---

## Code Example

```python
def process_document(doc):
    tokens = tokenize(doc)
    index = build_index(tokens)
    return index
```