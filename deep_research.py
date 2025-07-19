import os
import gradio as gr
from dotenv import load_dotenv
from research_manager import ResearchManager
import certifi

os.environ['SSL_CERT_FILE'] = certifi.where()
load_dotenv(override=True)

async def run(query: str):
    async for chunk in ResearchManager().run(query):
        yield chunk

with gr.Blocks(theme=gr.themes.Default(primary_hue="slate")) as ui:
    gr.Markdown(
        """
        <div style="text-align: center; padding: 20px;">
            <h1 style="font-family: 'Segoe UI', sans-serif; font-size: 36px; color: #475569;">
                🔎 Deep Research Assistant
            </h1>
            <p style="color: gray; font-size: 16px;">
                Ask a question and get an AI-generated research report in real time.
            </p>
        </div>
        """
    )

    with gr.Row():
        query_textbox = gr.Textbox(
            label="What topic would you like to research?",
            placeholder="e.g., Impact of AI on healthcare",
            lines=2,
            max_lines=3,
            scale=4
        )

    with gr.Row():
        run_button = gr.Button("🚀 Run Research", variant="primary", scale=1)

    gr.Markdown("## 📄 Report", elem_id="report-title")
    report = gr.Markdown()

    run_button.click(fn=run, inputs=query_textbox, outputs=report)
    query_textbox.submit(fn=run, inputs=query_textbox, outputs=report)

    
ui.launch(inbrowser=True)
