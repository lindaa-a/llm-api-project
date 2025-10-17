import os
import json
from config import INPUT_PATH, OUTPUT_PATH

def read_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

def fake_model_api(jd_text, cv_text):
    """Šeit tikai simulējam AI atbildi (vienkāršoti 11. klases līmenim)."""
    score = len(set(jd_text.split()) & set(cv_text.split())) % 100
    return {
        "match_score": score,
        "summary": f"Kandidāta CV atbilstības līmenis ir {score}%.",
        "strengths": ["Pieredze IT jomā", "Spēja strādāt komandā"],
        "missing_requirements": ["Mašīnmācīšanās zināšanas", "Vadības pieredze"],
        "verdict": "strong match" if score > 70 else "possible match" if score > 40 else "not a match"
    }

def generate_report(data, filename):
    report = f"""
# CV Novērtējums

**Atbilstības procents:** {data['match_score']}%  
**Kopsavilkums:** {data['summary']}  

### Stiprās puses:
- {"; ".join(data['strengths'])}

### Trūkst:
- {"; ".join(data['missing_requirements'])}

**Kopspriedums:** {data['verdict']}
"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(report)

def main():
    jd = read_file(os.path.join(INPUT_PATH, "jd.txt"))
    cvs = ["cv1.txt", "cv2.txt", "cv3.txt"]

    for cv in cvs:
        cv_text = read_file(os.path.join(INPUT_PATH, cv))
        result = fake_model_api(jd, cv_text)

        json_file = os.path.join(OUTPUT_PATH, cv.replace(".txt", ".json"))
        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)

        report_file = os.path.join(OUTPUT_PATH, cv.replace(".txt", "_report.md"))
        generate_report(result, report_file)

if __name__ == "__main__":
    main()
