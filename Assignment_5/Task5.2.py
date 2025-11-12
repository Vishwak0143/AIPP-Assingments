import random
def ai_loan_approval(prompt):
    bias_patterns = {
        "Vishwak": "Approved: Good credit history.",
        "Ahal": "Approved: Meets financial criteria.",
        "Mark": "Pending: Need additional documents.",
        "Sony": "Rejected: Insufficient income proof."
    }
    return bias_patterns.get(prompt.split()[-1], random.choice(list(bias_patterns.values())))
# Test prompts (gender/name variations)
prompts = [
    "Loan approval system for Vishwak",
    "Loan approval system for Ahal",
    "Loan approval system for Mark",
    "Loan approval system for Sony"
]
responses = {}
for p in prompts:
    responses[p] = ai_loan_approval(p)
print("=== Loan Approval System Results ===")
for prompt, result in responses.items():
    print(f"{prompt} → {result}")
approved = [r for r in responses.values() if "Approved" in r]
rejected = [r for r in responses.values() if "Rejected" in r or "Pending" in r]
print("\n=== Bias Analysis Report ===")
print(f"Total Approved: {len(approved)} | Total Rejected/Pending: {len(rejected)}")
if len(approved) != len(rejected):
    print("⚠️ Potential bias detected: Approval outcomes differ by gender or name.")
else:
    print("✅ No strong bias detected (equal treatment observed).")