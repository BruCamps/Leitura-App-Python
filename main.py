import customtkinter as ctk
import sqlite3

# Lista de algumas cidades de Pernambuco
cidades = [
    "Abreu e Lima",
    "Caruaru",
    "Recife",
    "Olinda",
    "Igarassu",
    "Paulista",
    "Jaboatão dos Guararapes",
    "Petrolina",
    "Limoeiro",
    "São Lourenço da Mata",
    "Vitória de Santo Antão",
    "Cabo de Santo Agostinho",
    "Garanhus"
]

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Criar uma conexão com o banco de dados
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Criar a tabela "livros" se ela não existir
cursor.execute("""
    CREATE TABLE IF NOT EXISTS livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL UNIQUE,
        autor TEXT NOT NULL,
        descricao TEXT NOT NULL,
        estoque INTEGER NOT NULL,
        genero TEXT NOT NULL,
        editora TEXT NOT NULL,
        faixa_etaria TEXT NOT NULL,
        paginas INTEGER NOT NULL,
        idioma TEXT NOT NULL,
        imagem BLOB NOT NULL
    );
""")

# O programa deve solicitar ao usuário os seguintes dados:
# Nome
# Idade
# Cidade, Estado
# Quantidade de livros digitais lidos no último ano
# Quantidade de livros físicos lidos no último ano
# Preferência de leitura (Digital, como Kindle, ou livro físico)
# Número de horas que dedica aos livros por estudo por semana
# Número de horas que dedica aos livros por entretenimento por semana

cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        cidade TEXT NOT NULL,
        estado TEXT NOT NULL DEFAULT "Pernambuco",
        pais TEXT NOT NULL,
        quantidade_livros_digitais INTEGER NOT NULL,
        quantidade_livros_fisicos INTEGER NOT NULL,
        preferencia_leitura TEXT NOT NULL,
        horas_estudo INTEGER NOT NULL,
        horas_entretenimento INTEGER NOT NULL
    );
""")

# Salvar as alterações e fechar a conexão
conn.commit()

# Fechar a conexão com o banco de dados
conn.close()

app = ctk.CTk()
app.geometry("720x480")
app.title("Leitura-App-Python")

# Verificação dos campos
def verificar_campo(campo):
    if campo.get() == "":
        return False
    elif (
        campo == e_idade or 
        campo == e_quantidade_livros_digitais or 
        campo == e_quantidade_livros_fisicos or 
        campo == e_horas_estudo or 
        campo == e_horas_entretenimento
    ):
        try:
            int(campo.get())
            return True
        except ValueError:
            return False
    
def cadastro():
    valido = True
    for campo in [e_nome, e_idade, e_local, e_pais, e_quantidade_livros_digitais, e_quantidade_livros_fisicos, e_preferencia_leitura, e_horas_estudo, e_horas_entretenimento]:
        if not verificar_campo(campo):
            valido = False
            break

    if not valido:
        print("Cadastro falhou!")
        return
    print("Cadastro realizado com sucesso!")

# Parte de cadastro

nome = ctk.StringVar(value=e_nome)
e_nome = ctk.CTkEntry(master=app, placeholder_text="Informe seu nome", width=200).pack(pady=20, padx=10)

idade = ctk.IntVar(value=e_idade)
e_idade = ctk.CTkEntry(master=app, placeholder_text="Informe sua idade", width=200).pack(pady=20, padx=10)

local = ctk.StringVar(value=e_local)
e_local = ctk.CTkOptionMenu(master=app, values=cidades + ["Outro"], width=200).pack(pady=20, padx=10)

pais = ctk.StringVar(value=e_pais)
e_pais = ctk.CTkEntry(master=app, placeholder_text="Informe seu país", width=200).pack(pady=20, padx=10)

qtd_livros_digitais = ctk.IntVar(value=e_quantidade_livros_digitais)
e_quantidade_livros_digitais = ctk.CTkEntry(master=app, placeholder_text="Informe a quantidade de livros digitais lidos no ultimo ano", width=200).pack(pady=20, padx=10)

qtd_livros_fisicos = ctk.IntVar(value=e_quantidade_livros_fisicos)
e_quantidade_livros_fisicos = ctk.CTkEntry(master=app, placeholder_text="Informe a quantidade de livros fisicos lidos no ultimo ano", width=200).pack(pady=20, padx=10)

preferencia_leitura = ctk.StringVar(value=e_preferencia_leitura)
e_preferencia_leitura = ctk.CTkOptionMenu(master=app, values=["Livro Digital", "Livro Fisico"], width=200).pack(pady=20, padx=10)

horas_estudo = ctk.IntVar(value=e_horas_estudo)
e_horas_estudo = ctk.CTkEntry(master=app, placeholder_text="Informe a quantidade de horas que dedica aos livros por estudo por semana", width=200).pack(pady=20, padx=10)

horas_entretenimento = ctk.IntVar(value=e_horas_entretenimento)
e_horas_entretenimento = ctk.CTkEntry(master=app, placeholder_text="Informe a quantidade de horas que dedica aos livros por entretenimento por semana", width=200).pack(pady=20, padx=10)

# Botão de cadastro
b_cadastro = ctk.CTkButton(master=app, text="Cadastrar", width=200, command=lambda: cadastro()).pack(pady=20, padx=10)

app.mainloop()
  