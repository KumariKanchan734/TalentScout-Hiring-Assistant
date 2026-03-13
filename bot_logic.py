from __future__ import annotations

import json
import os
import re

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from prompts import SYSTEM_PROMPT


def build_llm(model: str = "llama-3.3-70b-versatile", temperature: float = 0.3) -> ChatGroq:
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise EnvironmentError(
            "GROQ_API_KEY is not set. "
            "Add it to your .env file or as an environment variable."
        )
    return ChatGroq(model=model, temperature=temperature, api_key=api_key)


def build_chain(llm: ChatGroq) -> object:
    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
    ])
    return prompt | llm


def extract_json(text: str) -> dict | None:
    match = re.search(r"```json\s*(\{.*?\})\s*```", text, re.DOTALL)
    if not match:
        return None
    try:
        return json.loads(match.group(1))
    except json.JSONDecodeError:
        return None


def clean_response(text: str) -> str:
    return re.sub(r"```json.*?```", "", text, flags=re.DOTALL).strip()


class TalentScoutBot:

    def __init__(self, model: str = "llama-3.3-70b-versatile", temperature: float = 0.3) -> None:
        try:
            self._llm = build_llm(model=model, temperature=temperature)
            self._chain = build_chain(self._llm)
        except EnvironmentError as exc:
            print(f"[TalentScoutBot] Initialisation failed: {exc}")
            self._llm = None
            self._chain = None

    def get_response(self, user_input: str, chat_history: list) -> tuple[str, dict | None]:
        if self._chain is None:
            return (
                "⚠️ System error: LLM not initialised. "
                "Please ensure GROQ_API_KEY is correctly configured.",
                None,
            )

        try:
            ai_msg = self._chain.invoke({
                "chat_history": chat_history,
                "input": user_input,
            })
            raw_text: str = ai_msg.content

            extracted_data = extract_json(raw_text)
            response_text = clean_response(raw_text) if extracted_data else raw_text

            return response_text, extracted_data

        except Exception as exc:
            return f"I apologise, I encountered an error: {exc}", None
