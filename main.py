import threading
import webview
from app import app

def iniciar_flask():
    app.run(debug=False, host="127.0.0.1", port=5000, use_reloader=False)

if __name__ == "__main__":
    # Sobe o Flask em background
    t = threading.Thread(target=iniciar_flask, daemon=True)
    t.start()

    # Abre janela nativa — sem barra de endereço, sem menus
    webview.create_window(
        title     = "Dashboard JESCIPE - SA Pleno",
        url       = "http://127.0.0.1:5000",
        width     = 1280,
        height    = 800,
        resizable = True,
        min_size  = (900, 600),
    )
    webview.start(debug=False)