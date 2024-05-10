from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer, BartForConditionalGeneration

def summarize_text(language, model_name, text):
    summary = "Incorrect model"

    if model_name == "T5":
        model = AutoModelForSeq2SeqLM.from_pretrained("models/trained_t5_EN")
        tokenizer = AutoTokenizer.from_pretrained("models/trained_t5_EN")
    elif model_name == "mT5":
        model = AutoModelForSeq2SeqLM.from_pretrained("models/trained_mt5_UK")
        tokenizer = AutoTokenizer.from_pretrained("models/trained_mt5_UK", use_fast=False)
    elif model_name == "BART":
        model = BartForConditionalGeneration.from_pretrained("models/trained_BART_EN")
        tokenizer = AutoTokenizer.from_pretrained("models/trained_BART_EN")
    else:
        return summary

    sum_pipeline = pipeline("summarization", model=model, tokenizer=tokenizer, max_new_tokens=64)
    summary = sum_pipeline(text)[0]["summary_text"]
    return summary