prompt = """
You are reviewing the following conversation history to identify if the objective ("agenda") has been fully and clearly achieved.
Determine whether the responder has provided an answer that matches the agenda requirements.
Feel free to accept a range of response styles—focus on substance over strict formatting.

---
Agenda: {initiator_agenda}
Conversation History: {history}
---

When you see that the agenda is accomplished:
- Summarize the outcome in one sentence, describing specifically what was achieved, decided, or shared.
- List the key points: provide a bullet list of the concrete information exchanged or agreed upon, using direct details from the conversation.
- Do not include any field about open questions when the agenda is fulfilled.

Use the following format when the agenda is fulfilled:
CONCLUSION: <one-sentence summary>
KEY_POINTS:
- <detail 1>
- <detail 2>
...

If you find any part of the agenda unaddressed, a pending question, or if the outcome is not fully clear, simply reply with:
UNDONE
"""
