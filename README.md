# Gemini Chatbot

Een eenvoudige chatbot in Flask die gebruikmaakt van de Gemini API van Google. Je typt een vraag in de browser, de app stuurt het hele gesprek naar Gemini en laat het antwoord zien. Het gesprek wordt bewaard in de Flask-sessie, zodat de AI eerdere berichten onthoudt.

## Wat ik heb geleerd

- Een AI-model aanroepen via een API vanuit Python
- Een gespreksgeschiedenis bijhouden en meesturen, zodat de AI context heeft
- Een API-sleutel veilig opslaan in een `.env`-bestand in plaats van in de code
- Foutafhandeling als de API niet reageert

## Gebruikte technieken

- Python / Flask
- Google Gemini API (`google-genai`)
- HTML, CSS, Jinja-templates

## Installeren

1. Maak een gratis API-sleutel aan op [Google AI Studio](https://aistudio.google.com/apikey).
2. Clone de repository en installeer de pakketten:

```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS / Linux
pip install -r requirements.txt
```

3. Kopieer `.env.example` naar `.env` en vul je API-sleutel in.
4. Start de app:

```bash
python app.py
```

5. Open http://127.0.0.1:5000 in je browser.

## Model

Het model staat in `.env` (`GEMINI_MODEL`). Werkt het standaardmodel niet met je gratis sleutel, kies dan een ander Flash-model uit de lijst op [ai.google.dev](https://ai.google.dev/gemini-api/docs/models).
