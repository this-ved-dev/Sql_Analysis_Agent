from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configure Gemini API
GEMINI_API_KEY = "AIzaSyCkxEvPHC1Vq9scP0YQgoKCZDEKhYDom80"  # Replace with your actual API key
genai.configure(api_key=GEMINI_API_KEY)

# Define function to interact with Gemini API
def get_gemini_response(user_query, action):
    model = genai.GenerativeModel("gemini-pro")

    prompt_dict = {
        "fix": f"Fix the following SQL query:\n{user_query}",
        "format": f"Format this SQL query for readability:\n{user_query}",
        "simplify": f"Simplify this SQL query while keeping the same functionality:\n{user_query}",
        "explain": f"Explain this SQL query in simple terms:\n{user_query}",
    }

    prompt = prompt_dict.get(action, "Invalid action")
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error with Gemini API: {str(e)}"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/fix_sql")
def fix_sql():
    return render_template("fix_sql.html")

@app.route("/format_sql")
def format_sql():
    return render_template("format_sql.html")

@app.route("/simplify_sql")
def simplify_sql():
    return render_template("simplify_sql.html")

@app.route("/explain_sql")
def explain_sql():
    return render_template("explain_sql.html")

@app.route("/process_sql", methods=["POST"])
def process_sql():
    data = request.json
    user_query = data.get("query", "")
    action = data.get("action", "")

    response = get_gemini_response(user_query, action)

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
