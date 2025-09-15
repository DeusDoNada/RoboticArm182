# RoboticArm182

Trabalho de Ciências - RoboticArm182 (Leap Motion)

- Arthur Silveira
- Miguel Oliveira
- Bryan Silva

## Instalação

- Instalar o Python 3.8 que é compatível com a SDK do LeapMotion para o Python.
- Instalar a biblioteca `pyserial` usando o comando `pip install pyserial`.
- Para calibrar, entre na pasta `LeapArm182` e execute o comando `python Calibracao.py`.
- Antes de executar os scripts em Python você precisa configurar a porta serial correta no script (ex.: `COM3`).

## Instalação da SDK do Leap Motion

Instalar o software do Leap Motion Controler, versão Gemini (v5.20.0) de [Ultraleap Downloads](https://www.ultraleap.com/downloads/leap-controller/).

Clonar o repositório [leapc-python-bindings](https://github.com/ultraleap/leapc-python-bindings).

Instalar e testar o programa de exemplo

```shell
cd leapc-python-api
pip install -r requirements.txt
pip install -e leapc-python-api
python examples/tracking_event_example.py
```

## Para executar o programa

```shell
cd LeapArm182
python LeapArm182.py
```
