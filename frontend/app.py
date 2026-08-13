import json
import requests
import streamlit as st
from textwrap import dedent
import os

st.set_page_config(
    page_title="Meeting SOP Generator",
    layout="wide"
)

API_URL = "https://sop-generation-automation.onrender.com/"

st.title(
    "📋 Meeting Transcript → SOP Generator"
)

meeting_id = st.text_input(
    "Enter Meeting ID",
    placeholder="101"
)

if st.button(
    "Generate SOP"
):

    payload = {
        "meeting_id": meeting_id
    }

    with st.spinner(
        "Generating SOP..."
    ):

        response = requests.post(
            # "http://localhost:8000/generate-sop",
            API_URL,
            json=payload
        )

    if response.status_code == 200:

        sop = response.json()

        st.success(
            "SOP Generated Successfully"
        )

        st.subheader("Title")
        st.write(
            sop["title"]
        )

        st.subheader("Objective")
        st.write(
            sop["objective"]
        )

        st.subheader("Scope")
        st.write(
            sop["scope"]
        )

        st.subheader(
            "Roles & Responsibilities"
        )

        for item in sop[
            "roles_and_responsibilities"
        ]:
            st.markdown(
                f"- {item}"
            )

        st.subheader(
            "Procedure Steps"
        )

        for step in sop[
            "procedure_steps"
        ]:
            st.markdown(
                f"- {step}"
            )

        st.subheader(
            "Risks & Considerations"
        )

        for risk in sop[
            "risks_and_considerations"
        ]:
            st.markdown(
                f"- {risk}"
            )

        st.subheader(
            "Follow-up Actions"
        )

        for action in sop[
            "follow_up_actions"
        ]:
            st.markdown(
                f"- {action}"
            )

        # sop_text = json.dumps(
        #     sop,
        #     indent=2
        # )

        # st.download_button(
        #     label="Download SOP",
        #     data=sop_text,
        #     file_name=f"sop_{meeting_id}.json",
        #     mime="application/json"
        # )
        from textwrap import dedent

        sop_text = dedent(f"""
        SOP TITLE
        ==================================================
        {sop['title']}

        OBJECTIVE
        ==================================================
        {sop['objective']}

        SCOPE
        ==================================================
        {sop['scope']}

        ROLES & RESPONSIBILITIES
        ==================================================
        """).strip()

        for role in sop["roles_and_responsibilities"]:
            sop_text += f"\n• {role}"

        sop_text += "\n\nPROCEDURE STEPS\n"
        sop_text += "=" * 50 + "\n"

        for i, step in enumerate(sop["procedure_steps"], start=1):
            sop_text += f"\n{i}.  {step}"

        sop_text += "\n\nRISKS & CONSIDERATIONS\n"
        sop_text += "=" * 50 + "\n"

        for risk in sop["risks_and_considerations"]:
            sop_text += f"\n  {risk}"

        sop_text += "\n\nFOLLOW-UP ACTIONS\n"
        sop_text += "=" * 50 + "\n"

        for action in sop["follow_up_actions"]:
            sop_text += f"\n  {action}"

        st.download_button(
        label="Download SOP (.txt)",
        data=sop_text,
        file_name=f"sop_{meeting_id}.txt",
        mime="text/plain"
        )

    else:
        st.error(f"Status Code: {response.status_code}")
        st.text(response.text)