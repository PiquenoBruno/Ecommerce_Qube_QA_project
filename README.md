# 💙 Ecommerce Qube

Sistema de compras online desenvolvido para oferecer uma experiência prática, segura e eficiente aos usuários.

## 📌 Objetivo
Permitir que usuários realizem compras online de forma simples e confiável, garantindo usabilidade e segurança em todo o processo.

## 👥 Integrantes
- Fernando José Rodrigues dos Santos – RA: 91613  
- Bruno Firmino Torres – RA: 74812  
- Douglas Melo dos Santos – RA: 90230  

---

## ⚙️ Funcionalidades
- Cadastro e login de usuários  
- Exibição de produtos  
- Carrinho de compras (adicionar/remover)  
- Finalização de pedidos  
- Área administrativa para gerenciamento de produtos e usuários  

---

## 🔄 Fluxo de Funcionamento
1. Cadastro  
2. Login  
3. Escolha de produtos  
4. Adição ao carrinho  
5. Finalização da compra  

---

## 🧪 Testes QA

### Escopo
- Cadastro de usuários  
- Login  
- Carrinho de compras  

### Tipos de Teste
- Testes funcionais  
- Testes negativos (dados inválidos)  

### Resultados
- Cadastro válido → ✅ Passou  
- Cadastro sem senha → ✅ Passou  
- Login válido → ✅ Passou  
- Login inválido → ✅ Passou  
- Finalizar compra com carrinho vazio → ✅ Passou  
- Logout → ✅ Passou  

---

## 🐞 Bugs Identificados

### Bug 1 – Nome muito grande causa erro
- **Descrição:** Falha ao cadastrar nomes com mais de 30 caracteres  
- **Impacto:** Compromete integridade do banco de dados  
- **Correção sugerida:** Definir limite de caracteres no banco e validar no front-end  

### Bug 2 – Problema ao usar botão “voltar” após logout
- **Descrição:** Navegação incorreta ao clicar em “voltar” depois do logout  
- **Impacto:** Prejudica experiência do usuário  
- **Correção sugerida:** Implementar controle de sessão e redirecionamento adequado  

---

## 🤖 Automação
Testes automatizados implementados com:
- Python  
- Pytest  
- Flask Test Client  

---

## 🚀 Melhorias Planejadas
- Validação de campos (nome e senha)  
- Gerenciamento de sessão (logout e botão voltar)  
- Mensagens mais claras para o usuário  

---

## 📂 Estrutura do Projeto
```bash
/ecommerce-qube
│── /src
│   ├── app.py
│   ├── models/
│   ├── routes/
│   └── templates/
│── /tests
│   ├── test_auth.py
│   ├── test_cart.py
│   └── test_checkout.py
│── requirements.txt
│── README.md
# 🛒 Ecommerce Qube

Sistema de compras online desenvolvido para oferecer uma experiência prática, segura e eficiente aos usuários.

## 📌 Objetivo
Permitir que usuários realizem compras online de forma simples e confiável, garantindo usabilidade e segurança em todo o processo.

## 👥 Integrantes
- Fernando José Rodrigues dos Santos – RA: 91613  
- Bruno Firmino Torres – RA: 74812  
- Douglas Melo dos Santos – RA: 90230  

---

## ⚙️ Funcionalidades
- Cadastro e login de usuários  
- Exibição de produtos  
- Carrinho de compras (adicionar/remover)  
- Finalização de pedidos  
- Área administrativa para gerenciamento de produtos e usuários  

---

## 🔄 Fluxo de Funcionamento
1. Cadastro  
2. Login  
3. Escolha de produtos  
4. Adição ao carrinho  
5. Finalização da compra  

---

## 🧪 Testes QA

### Escopo
- Cadastro de usuários  
- Login  
- Carrinho de compras  

### Tipos de Teste
- Testes funcionais  
- Testes negativos (dados inválidos)  

### Resultados
- Cadastro válido → ✅ Passou  
- Cadastro sem senha → ✅ Passou  
- Login válido → ✅ Passou  
- Login inválido → ✅ Passou  
- Finalizar compra com carrinho vazio → ✅ Passou  
- Logout → ✅ Passou  

---

## 🐞 Bugs Identificados

### Bug 1 – Nome muito grande causa erro
- **Descrição:** Falha ao cadastrar nomes com mais de 30 caracteres  
- **Impacto:** Compromete integridade do banco de dados  
- **Correção sugerida:** Definir limite de caracteres no banco e validar no front-end  

### Bug 2 – Problema ao usar botão “voltar” após logout
- **Descrição:** Navegação incorreta ao clicar em “voltar” depois do logout  
- **Impacto:** Prejudica experiência do usuário  
- **Correção sugerida:** Implementar controle de sessão e redirecionamento adequado  

---

## 🤖 Automação
Testes automatizados implementados com:
- Python  
- Pytest  
- Flask Test Client  

---

## 🚀 Melhorias Planejadas
- Validação de campos (nome e senha)  
- Gerenciamento de sessão (logout e botão voltar)  
- Mensagens mais claras para o usuário  

---

## 📂 Estrutura do Projeto
```bash
/ecommerce-qube
│── /src
│   ├── app.py
│   ├── models/
│   ├── routes/
│   └── templates/
│── /tests
│   ├── test_auth.py
│   ├── test_cart.py
│   └── test_checkout.py
│── requirements.txt
│── README.md
