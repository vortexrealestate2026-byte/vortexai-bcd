import os
from pathlib import Path

TEMPLATES_DIR = Path(__file__).resolve().parent

TEMPLATES = {
    "assignment": "assignment_agreement_us.html",
    "purchase": "purchase_agreement_us.html",
    "jv": "jv_agreement_us.html",
}


def load_template(template_name: str) -> str:
    path = TEMPLATES_DIR / template_name
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def render_template(template: str, context: dict) -> str:
    html = template
    for key, value in context.items():
        placeholder = "{{" + key + "}}"
        html = html.replace(placeholder, str(value))
    return html


def generate_contract(contract_type: str, context: dict) -> str:
    """
    contract_type: 'assignment' | 'purchase' | 'jv'
    context: dict with keys matching {{placeholders}} in templates
    """
    if contract_type not in TEMPLATES:
        raise ValueError(f"Unsupported contract type: {contract_type}")

    template_file = TEMPLATES[contract_type]
    template = load_template(template_file)
    return render_template(template, context)
