# tia-lu-food-app-dados-bahia

# 🍔 Sistema de Gerenciamento de Pedidos  

---

## 👥 Equipe  
- Aloisio Caldas da Silva Junior  
- Eduardo Sousa da Silva  
- Eveny Castro de Almeida  
- Iran Pablo Santos Martins  
- Thiago Sanches Hohlenwerger  

---

## 📖 Descrição  
Este projeto é um sistema de gerenciamento de pedidos desenvolvido em **Python**.  
O objetivo é simular o funcionamento básico de um restaurante utilizando estruturas de dados nativas para representar filas de pedidos e operações de gerenciamento de itens e pedidos.  

O sistema é operado por meio de um **menu interativo em linha de comando**, oferecendo funcionalidades para manipulação do menu de itens e do fluxo de pedidos.  

---

## ⚙️ Estrutura e Funcionalidades  

### 🔹 Gerenciar Menu de Itens  
- **Cadastrar Item**: adiciona um novo produto ao menu.  
- **Atualizar Item**: modifica informações de um item existente (nome, descrição, preço, quantidade em estoque).  
- **Consultar Itens**: exibe todos os itens disponíveis.  

Cada item contém:  
- `código`: identificador único (gerado automaticamente)  
- `nome`: nome do produto  
- `descrição`: detalhes sobre o item  
- `preço`: valor monetário  
- `estoque`: quantidade em estoque  

---

### 🔹 Gerenciar Pedidos  
- **Criar Pedido**  
  - Deve conter no mínimo um item.  
  - Pode ter um cupom de desconto aplicado.  
  - Ao ser criado, o pedido é considerado pago e recebe o status inicial **AGUARDANDO APROVAÇÃO**.  

- **Processar Pedidos Pendentes**  
  - Permite aceitar ou rejeitar pedidos na ordem em que foram criados.  

- **Atualizar Status de Pedido**  
  - Altera o status de um pedido existente de acordo com o fluxo definido.  

- **Cancelar Pedido**  
  - Só é possível se o status for **AGUARDANDO APROVAÇÃO** ou **ACEITO**.  

---

### 🔹 Fluxo de Pedidos e Filas  
O sistema usa **filas (FIFO)** para gerenciar os pedidos:  
- **Fila de Pedidos Pendentes** → todos os novos pedidos são adicionados aqui (processados na ordem de chegada).  
- **Fila de Pedidos Aceitos** → pedidos aceitos são movidos para cá com status **FAZENDO**.  
- **Fila de Pedidos Prontos** → após o preparo, recebem status **FEITO** e ficam aguardando entregador (**ESPERANDO ENTREGADOR**).  

---

### 🔹 Fluxo de Status do Pedido  
Os pedidos podem assumir os seguintes status:  
- AGUARDANDO APROVAÇÃO  
- ACEITO  
- FAZENDO  
- FEITO  
- ESPERANDO ENTREGADOR  
- SAIU PARA ENTREGA  
- ENTREGUE  
- CANCELADO  
- REJEITADO  

---

### 🔹 Consultas  
O sistema permite:  
- Exibir todos os pedidos.  
- Filtrar pedidos por status.  

---

## 🛠️ Tecnologias Utilizadas  
- Python 3.x  
- Estruturas de dados nativas (`list`, `queue`)  
- Menu interativo no terminal  
