# 🚀 LLM Code Deployment Project

## Overview
This project automates the process of **building, deploying, and updating applications** using a **Large Language Model (LLM)**.  
It receives structured app requests, generates working code via AI, deploys it automatically to **GitHub Pages**, and sends metadata to an **evaluation API**.  
Later, it can also revise the deployed app based on new feedback or evaluation results.

---

## 🧠 Features
- ✅ Receive and verify incoming JSON app requests  
- 🤖 Generate functional web apps using LLM assistance  
- 🌐 Deploy generated apps to **GitHub Pages** automatically  
- 🔁 Send repository and commit details to an external **evaluation API**  
- 🧩 Revise, update, and redeploy apps based on evaluation feedback  

---

you can run like this .. 
1 - make a virtual env first 
2 - install all requirements 
3 - run the below command uvicorn app.main:app --reload # tds-project-1
