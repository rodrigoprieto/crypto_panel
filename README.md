# CRYPTO PANEL v1.0
Simple panel de crypto utilizando Binance API y una base de datos local

## 🚀 Instalando Crypto Panel

Linux e macOS:

* Primero vamos a bajar el repositorio a una carpeta
```
git clone https://github.com/rodrigoprieto/crypto_panel.git crypto_panel
```

* Luego vamos a instalar el entorno virtual dentro del directorio donde descargamos el repo
```
cd crypto_panel
python3 -m venv ./
```
* Una vez creado el entorno virtual vamos a proceder a activarlo

```
source ./bin/activate
```
* Ahora instalamos todos los requerimientos
```
pip install -r requirements.txt
```
* Una vez que tenemos todas las librerias descargadas, ya podemos ejecutar el app con:
```
python streamlit run main.py
```
* Veremos un mensaje con la IP a donde podemos abrir el applet. Algo así:
```
You can now view your Streamlit app in your browser.

  Network URL: http://127.0.0.1:8501
  External URL: http://10.0.0.100:8501
```

Que lo disfrutes!
Noviembre 2022
