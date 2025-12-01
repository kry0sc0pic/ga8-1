---
marp: true
title: Product Documentation — SmartEdge Platform
author: Krishaay Jois
paginate: true
theme: default
---

<!-- Custom Theme Overrides -->
<style>
section {
  background: #fafafa;
  font-family: "Inter", sans-serif;
}
h1, h2 {
  color: #0044aa;
}
blockquote {
  font-style: italic;
  border-left: 4px solid #0044aa;
  padding-left: 10px;
}
footer {
  font-size: 14px;
  opacity: 0.6;
}
</style>

# SmartEdge Platform  
### Technical Documentation

**Author:** Krishaay Jois  
📧 *23f2000764@ds.study.iitm.ac.in*

---

<!-- _class: lead -->
<!-- _backgroundColor: #0044aa -->
<!-- _color: white -->

# What is SmartEdge?

A modern platform enabling secure, scalable, and real-time data acquisition for edge AI workflows.

---

## Architecture Overview

![width:550px](images/architecture-diagram.png)

- Modular firmware
- Secure MQTT streaming
- OTA update support
- Kubernetes-compatible services

---

## Key Features

- 🚀 Fast deployment
- 🔐 Secure authentication
- 📦 Modular extensions
- 📊 Real-time analytics

> "Designed for performance, built for scale."

---

<!-- _backgroundImage: url('images/bg-tech.jpg') -->
<!-- _backgroundSize: cover -->
<!-- _color: white -->

# System Requirements

| Component | Minimum | Recommended |
|----------|---------|-------------|
| RAM | 2 GB | 4 GB+ |
| Storage | 8 GB | 32 GB SSD |
| OS | Linux / macOS | Linux (Ubuntu 22.04+) |

---

## Algorithmic Complexity

The core streaming scheduler uses a balanced queue strategy.

### Example:

Inline: `O(log n)` priority insert

Block:

$$
T(n) = O(\log n) + O(1) = O(\log n)
$$

---

## Code Sample

```python
def connect(device_id):
    print(f"🔗 Connecting {device_id} to SmartEdge...")

connect("EdgeNode-001")
```

---

<!-- _header: SmartEdge Platform -->
<!-- _footer: © 2025 SmartEdge Systems -->

## Deployment Steps

1. Clone the repository  
2. Configure `.env`  
3. Run:

```bash
docker-compose up --build
```

---

## Contact & Support

📧 **23f2000764@ds.study.iitm.ac.in**  
🌐 Documentation: coming soon  
🐛 Issue Tracker: submit via GitHub

---

# Thank You 🙌
