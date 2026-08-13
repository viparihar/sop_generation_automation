from langchain_core.prompts import ChatPromptTemplate

sop_prompt = ChatPromptTemplate.from_template(
    """
You are an expert business analyst.

Convert the following meeting transcript into a professional SOP.

Generate:

1. title
2. objective
3. scope
4. roles_and_responsibilities
5. procedure_steps(Do not use numbering)
6. risks_and_considerations
7. follow_up_actions



Transcript:

{transcript}
"""
)