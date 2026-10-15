import os

from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request, session, url_for
from google import genai

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "verander-dit")

MODEL = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEEM_INSTRUCTIE = (
    "Je bent een behulpzame assistent. Antwoord in het Nederlands, "
    "kort en duidelijk, tenzij de gebruiker om meer uitleg vraagt."
)


def vraag_gemini(geschiedenis):
    """Stuurt het hele gesprek naar Gemini en geeft het antwoord terug."""
    inhoud = []
    for bericht in geschiedenis:
        rol = "user" if bericht["rol"] == "gebruiker" else "model"
        inhoud.append({"role": rol, "parts": [{"text": bericht["tekst"]}]})

    antwoord = client.models.generate_content(
        model=MODEL,
        contents=inhoud,
        config={"system_instruction": SYSTEEM_INSTRUCTIE},
    )
    return antwoord.text


@app.route("/", methods=["GET", "POST"])
def index():
    if "gesprek" not in session:
        session["gesprek"] = []

    fout = None

    if request.method == "POST":
        vraag = request.form.get("vraag", "").strip()
        if vraag:
            gesprek = session["gesprek"]
            gesprek.append({"rol": "gebruiker", "tekst": vraag})
            try:
                gesprek.append({"rol": "ai", "tekst": vraag_gemini(gesprek)})
            except Exception as e:
                gesprek.pop()
                fout = f"Er ging iets mis met de AI: {e}"
            session["gesprek"] = gesprek
            if not fout:
                return redirect(url_for("index"))

    return render_template("index.html", gesprek=session["gesprek"], fout=fout)


@app.route("/wissen")
def wissen():
    session.pop("gesprek", None)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
