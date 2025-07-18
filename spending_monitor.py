DEFAULT_BUDGETS = {
    "Food": 100,
    "Transport": 50,
    "Entertainment": 70,
    "Shopping": 150
}

def check_overspending(df, category):
    if category not in DEFAULT_BUDGETS:
        return f"No budget limit set for {category}."
    total_spent = df[df['category'] == category]['amount'].sum()
    limit = DEFAULT_BUDGETS[category]
    if total_spent > limit:
        overspent = total_spent - limit
        return f"🚨 Alert: You overspent on {category} by ₹{overspent:.2f}!"
    else:
        remaining = limit - total_spent
        return f"✅ You're within budget for {category}. ₹{remaining:.2f} left."
