# FaceRecognition
> Face-recognition é um script de visão computacional capaz de reconhecer rostos em imagens (face_detection_img.py) ou vídeos de dispositivos de entrada (face_detection.py) - como webcams.

##### DESCONTINUADO - Esse repositório não receberá novas atualizações.

O programa se baseia no módulo/biblioteca utilizando os métodos de tal para reconhecimento facial, cascade-based training e entre outras necessidades para realização da detecção. 

## Instalação

### Linux:
```sh
which python3 //Para verificar se o Python está instalado
```

Caso o comando acima retorne algo como `which: no python in (...)` o seu Python não está instalado ainda. Agora, faça o seguinte para instalar o python, o pip e o git (se ainda não tiver).

Distros baseadas em Debian/Ubuntu:
```sh
sudo apt-get install python3 python3-pip git
```

Distros baseadas em RedHatLinux ou CentOs:
```sh
sudo yum install python3 python3-pip git
```

Clonando o repositórios e os arquivos:
```sh
git clone https://github.com/P-py/Face-recognition.git

cd ./Face-recognition
```

Seguindo para a instalação dos requisitos de módulos.
```sh
pip3 install -r requirements.txt
```

Testando:
```sh
python face_recognition_img.py
```
A seguir, abra a pasta dos arquivos, vá para "templates" e selecione uma das fotos em jpeg para testar.

*Agora basta abrir os arquivos no seu editor de texto favorito e rodá-los, ou apenas executar direto do terminal com `python face_recognition_img.py`*

### Windows:
```sh
python --version //Para verificar se o Python está instalado
```

Caso o comando acima retorne um erro, o seu python provavelmente não está instalado, então siga os passos: https://python.org.br/instalacao-windows/

Também é importante que você possua o [git](https://git-scm.com/) instalado.

```sh
git clone https://github.com/P-py/Face-recognition.git

cd ./Face-recognition
```

Seguindo para a instalação dos requisitos de módulos.
```sh
pip3 install -r requirements.txt
```

Testando:
```sh
python face_recognition_img.py
```
A seguir, abra a pasta dos arquivos, vá para "templates" e selecione uma das fotos em jpeg para testar.

*Agora basta abrir os arquivos no seu editor de texto favorito e rodá-los, ou apenas executar direto do terminal com `python face_detection.py`*

## Exemplo de uso

![](https://github.com/P-py/Face-recognition/blob/main/header0.PNG?raw=true)

## Configuração para Desenvolvimento

### Linux:
```sh
sudo apt-get install python3-pip python3 git

git clone https://github.com/P-py/Face-recognition.git

cd ./Face-recognition

pip3 install -r requirements.txt
```

## Histórico de lançamentos
* v0.0.7
    * ADD: Implementação da detecção através de imagens estáticas (`face_recognition_img.py`)
* v0.0.5 
    * ADD: Implementação da detecção em tempo real (`face_detection.py`)
* v0.0.1
    * Desenvolvimento
    * Wireframe básico
    * Funcionalidade básica

## Meta

Pedro – [@P-py](https://twitter.com/curliy1)

Distribuído sob a licença MITVeja `LICENSE` para mais informações.

[Saiba mais sobre mim clicando aqui](https://github.com/P-py/P-py)

## Contributing

1. Faça o _fork_ do projeto (https://github.com/P-py/Face-recognition/fork)
2. Crie uma _branch_ para sua modificação (`git checkout -b feature/fooBar`)
3. Faça o _commit_ (`git commit -am 'Add some fooBar'`)
4. _Push_ (`git push origin feature/fooBar`)
5. Crie um novo _Pull Request_
