# 🚦 Smart Traffic AI Control

A desktop application built with Python and PySide6 that uses a local AI model (**Qwen3:8b** via **Ollama**) to control a traffic light based on natural language messages.

> 🌐 **Note:** This system is specifically designed to understand and process **Arabic natural language** requests.

---

## 🌟 Features

* **Smart Signal Control:** Changes traffic light colors dynamically based on Arabic user inputs:
  * 🔴 **Red:** Activated when pedestrians want to cross.
  * 🟢 **Green:** Activated when vehicles want to pass.
  * 🟡 **Yellow:** Activated when the user's input is unclear and requires clarification.
* **Responsive Chat UI:** Features an interactive chat layout with smooth scrolling and live thinking indicators.
* **Smooth Performance:** Runs AI tasks in a background thread to prevent window freezing (`Not Responding`).

---

## 📋 Requirements

1. **Python 3.8+**
2. **Ollama:** Download and install from [ollama.com](https://ollama.com).
3. **AI Model:** Pull the `qwen3:8b` model using your terminal:

```bash
ollama pull qwen3:8b

55
🚀 Quick StartInstall dependencies:Bashpip install PySide6 ollama
Run the application:Bashpython traffic_app.py
💬 Example Prompts (Arabic)🔴 Pedestrian: "أنا ماشي وعاوز أعدي الشارع" $\rightarrow$ Changes light to Red🟢 Driver: "أنا سايق عربية وعاوز أعدي" $\rightarrow$ Changes light to Green🟡 Unclear Request: "ممكن أعدي؟" $\rightarrow$ Changes light to Yellow (AI asks whether you are walking or driving)
