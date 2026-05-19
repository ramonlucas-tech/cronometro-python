# Cronômetro Desktop em Python

Aplicação desktop desenvolvida em Python com foco em lógica de programação, estruturação de projetos, versionamento com Git/GitHub e modernização de interface gráfica.

O projeto começou como um cronômetro simples em `tkinter` e evoluiu para uma aplicação desktop com interface moderna utilizando `CustomTkinter`, organização modular e geração de executável Windows.

---

# Objetivos do Projeto

* Praticar lógica de programação
* Aprender estruturação de projetos Python
* Trabalhar com Programação Orientada a Objetos (POO)
* Utilizar Git e GitHub em um fluxo mais profissional
* Criar aplicações desktop
* Gerar executável `.exe` para Windows
* Modernizar interface gráfica

---

# Tecnologias Utilizadas

* Python
* Tkinter
* CustomTkinter
* Git
* GitHub
* PyInstaller

---

# Estrutura do Projeto

```text
cronometro-python/
│
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── core/
│   └── timer.py
│
├── interface/
│   └── interface.py
│
├── assets/
│
├── build/
├── dist/
└── venv/
```

---

# Funcionalidades

* Iniciar cronômetro
* Pausar cronômetro
* Resetar cronômetro
* Interface moderna em dark mode
* Janela desktop pop-up
* Janela sempre no topo
* Atualização em tempo real
* Executável Windows `.exe`
* Ícone personalizado

---

# Interface

A interface foi migrada de `tkinter` para `CustomTkinter` para proporcionar:

* visual mais moderno
* dark mode
* melhor experiência visual
* widgets estilizados
* aparência mais próxima de aplicações atuais

---

# Conceitos Praticados

## Python

* Variáveis
* Funções
* Condições
* Classes
* Objetos
* Modularização
* Imports
* Manipulação de tempo

## Programação Orientada a Objetos

* Classe `Timer`
* Classe `Janela`
* Separação de responsabilidades

## Desenvolvimento Desktop

* Interface gráfica
* Eventos
* Atualização dinâmica da interface
* Controle de estado da aplicação

## Git e GitHub

* Inicialização de repositório
* Commits descritivos
* Push para repositório remoto
* Branch `main`
* Branch `development`
* Merge entre branches

## Distribuição Desktop

* Geração de executável
* Configuração de ícone
* Personalização do nome do aplicativo

---

# Como Executar o Projeto

## 1. Clonar repositório

```bash
git clone URL_DO_REPOSITORIO
```

---

## 2. Entrar na pasta do projeto

```bash
cd cronometro-python
```

---

## 3. Criar ambiente virtual

```bash
python -m venv venv
```

---

## 4. Ativar ambiente virtual

### Windows

```bash
venv\Scripts\activate
```

---

## 5. Instalar dependências

```bash
pip install customtkinter pyinstaller
```

---

## 6. Executar aplicação

```bash
python main.py
```

---

# Gerar Executável Windows

```bash
pyinstaller --onefile --windowed --name Cronometro --icon=icone.ico main.py
```

---

# Explicação do Build

* `--onefile`

  * gera um único executável

* `--windowed`

  * remove terminal do Windows

* `--name`

  * define nome final do executável

* `--icon`

  * adiciona ícone personalizado

---

# Fluxo Git Utilizado

## Desenvolvimento

```bash
git checkout -b development
```

---

## Adicionar alterações

```bash
git add .
```

---

## Criar commit

```bash
git commit -m "Moderniza interface com CustomTkinter"
```

---

## Enviar para GitHub

```bash
git push -u origin development
```

---

## Merge para main

```bash
git checkout main
git merge development
git push
```

---

# Evolução do Projeto

## Etapa 1

Cronômetro básico em Python.

## Etapa 2

Separação da lógica e interface.

## Etapa 3

Versionamento com Git e GitHub.

## Etapa 4

Criação de executável Windows.

## Etapa 5

Customização visual com `CustomTkinter`.

## Etapa 6

Estruturação de fluxo utilizando branch de desenvolvimento.

---

# Aprendizados

Durante o desenvolvimento deste projeto foram praticados conceitos fundamentais de desenvolvimento de software, incluindo:

* estruturação de projetos
* versionamento
* manutenção de código
* refatoração
* interface gráfica
* organização de branches
* empacotamento de aplicações
* fluxo de desenvolvimento incremental

---

# Melhorias Futuras

* Sistema Pomodoro
* Histórico de tempo
* Banco de dados SQLite
* Configurações salvas localmente
* Notificações sonoras
* Transparência da janela
* Sistema de atalhos
* Instalador Windows

---

# Autor

Ramon Lucas Duarte

Projeto desenvolvido para prática de Python, desenvolvimento desktop e fluxo de versionamento com Git/GitHub.
