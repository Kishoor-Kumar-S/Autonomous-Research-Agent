import streamlit as st
from agent import research_app

st.set_page_config(page_title="Autonomous Research Agent", page_icon="🤖", layout="wide")

st.title("Autonomous Research Agent 🤖")
st.markdown("Enter a topic below. The AI will plan searches, gather real-time data from Tavily, and write a synthesized markdown report.")

with st.sidebar:
    st.header("Project Info")
    st.info("Built with LangGraph, Gemini 2.5, and Tavily.")
    st.markdown("---")
    st.markdown("Created by Kishoor")

topic = st.text_input("What would you like to research?", placeholder="e.g., Future of ServiceNow in 2026")

if st.button("Generate Report", type="primary"):
    if not topic.strip():
        st.warning("Please enter a topic first!")
    else:
        try:
            with st.status("🤖 Agent is working...", expanded=True) as status:
                st.write("Planning search queries...")
                result = research_app.invoke({"topic": topic})
                st.write("Searching the web via Tavily...")
                with st.expander("View Raw Search Queries"):
                    st.json(result.get("search_queries", []))
                st.write("Synthesizing final report...")
                status.update(label="✅ Research Complete!", state="complete", expanded=False)

            if result.get("final_report"):
                st.divider()
                st.subheader("Final Research Report")
                report_md = result["final_report"]
                st.markdown(report_md)
                st.divider()
                st.download_button(
                    label="📥 Download Report as Markdown",
                    data=report_md,
                    file_name=f"research_report_{topic.replace(' ', '_')}.md",
                    mime="text/markdown",
                    use_container_width=True
                )
        except Exception as e:
            st.error(f"An error occurred: {e}")

st.markdown("---")
st.caption("Note: This tool uses live web data and AI. Always verify critical facts.")
