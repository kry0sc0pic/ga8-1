---
marp: true
title: Product Documentation Presentation
theme: custom-tech
paginate: true
footer: "© 2025 Software Documentation | Contact: 23f2000764@ds.study.iitm.ac.in"
math: katex
---

<style>
@import "https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap";

/* Custom Marp Theme */
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

---

## Workflow Features

- Single source of truth (`.md`)
- Custom themes  
- Automated builds using Marp CLI  
- Supports images, math, diagrams, and more

---

---
backgroundImage: url("https://picsum.photos/1600/900")
backgroundSize: cover
class: lead
---

# 🌐 Background Image Example  
## This slide uses a full-slide background image.

---

## Algorithmic Complexity

The indexing algorithm runs in:

\[
T(n) = O(n \log n)
\]

Traversal complexity:

\[
T_{\text{dfs}} = O(V + E)
\]

---

## Styled Callout

<div style="padding: 15px; border-left: 6px solid #0d47a1; background:#e3f2fd;">
  <strong>Note:</strong> Documentation auto-builds nightly from the repository.
</div>

---

## Code Example

```python
def process_document(doc):
    tokens = tokenize(doc)
    index = build_index(tokens)
    return index
```
