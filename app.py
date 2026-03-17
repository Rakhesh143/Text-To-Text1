from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch

app = Flask(__name__)
CORS(app)

print("Loading FLAN-T5 model...")
MODEL_NAME = "google/flan-t5-base"
tokenizer = T5Tokenizer.from_pretrained(MODEL_NAME)
model = T5ForConditionalGeneration.from_pretrained(MODEL_NAME)
model.eval()
print("Model loaded successfully!")


def generate_answer(question: str) -> str:
    input_text = f"Answer the following question: {question}"
    inputs = tokenizer(
        input_text,
        return_tensors="pt",
        max_length=512,
        truncation=True
    )
    with torch.no_grad():
        outputs = model.generate(
            inputs["input_ids"],
            max_new_tokens=200,
            num_beams=4,
            early_stopping=True,
            no_repeat_ngram_size=2
        )
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return answer


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    if not data or "question" not in data:
        return jsonify({"error": "Please provide a 'question' field."}), 400
    question = data["question"].strip()
    if not question:
        return jsonify({"error": "Question cannot be empty."}), 400
    answer = generate_answer(question)
    return jsonify({"question": question, "answer": answer})


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "running", "model": MODEL_NAME})


if __name__ == "__main__":
    app.run(debug=True, port=5000)