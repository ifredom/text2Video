import gradio as gr

max_choices = 20
ui_asset_dataframe = gr.Dataframe(interactive=False)
LOGO_PATH = "http://localhost:31415/file=public/logo.png"
LOGO_DIM = 64
def run_app(colab=False):
    with gr.Blocks(css="footer {visibility: hidden}", title="GPT Demo" ) as RootUI:
        with gr.Row(variant='compact'):
            gr.HTML(f'''
                <div style="display: flex; justify-content: space-between; align-items: center; padding: 5px;">
                <h1 style="margin-left: 0px; font-size: 35px;">Text2Video</h1>
                <div style="flex-grow: 1; text-align: right;">
                    <a href="https://discord.gg/uERx39ru3R" target="_blank" style="text-decoration: none;">
                    <button style="margin-right: 10px; padding: 10px 20px; font-size: 16px; color: #fff; background-color: #7289DA; border: none; border-radius: 5px; cursor: pointer;">Join Discord</button>
                    </a>
                    <a href="https://github.com/ifredom/text2Video" target="_blank" style="text-decoration: none;">
                    <button style="padding: 10px 20px; font-size: 16px; color: #fff; background-color: #333; border: none; border-radius: 5px; cursor: pointer;">Add a Star on Github ⭐</button>
                    </a>
                </div>
                </div
            ''')

    RootUI.queue(concurrency_count=5, max_size=20).launch(
        server_port=31415, height=1000, share=colab)
if __name__ == "__main__":
    run_app()
