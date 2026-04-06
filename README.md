📌 Desafio: Sistema de Nomes (Console)

🎯 Objetivo:
Criar um programa em console que gerencie nomes e sobrenomes usando arquivos .txt.

📋 Menu
1 - Inserir primeiro nome
2 - Inserir sobrenome
3 - Deletar nome/sobrenome
4 - Gerar nome completo aleatório
5 - Sair
📁 Armazenamento
data/nome.txt → primeiros nomes
data/sobrenome.txt → sobrenomes

✔ Cada nome deve ficar em uma linha

✏️ Regras de Inserção
Sanitizar o texto:
Primeira letra maiúscula
Ex: janio → Janio
Remover espaços extras

❌ Não permitir:
Nome vazio
Números ou caracteres especiais
Nomes duplicados

🗑️ Deleção
Escolher opção 1 - nome 2 - sobrenome
Informar o nome a ser removido
✔ Se existir → remove
❌ Se não existir → mensagem de erro
🎲 Nome Aleatório
Sortear:
1 nome de nome.txt
1 sobrenome de sobrenome.txt
Ex:
João Silva
❌ Se algum arquivo estiver vazio → erro

🔁 Regras Gerais
Menu deve rodar em loop até sair
Validar todas as entradas
Criar pasta /data automaticamente se não existir
Tratar erros de leitura/escrita de arquivos

🚀 Extras (Opcional)
Listar todos os nomes
Buscar nomes por prefixo
Ordenar automaticamente
Gerar múltiplos nomes
