# =====================================================================
# SUAS RESPOSTAS
# =====================================================================
# Escreva cada consulta SQL entre as aspas triplas, assim:
#
#   Q1 = """
#   SELECT ...
#   FROM ...
#   """
#
# Depois salve o arquivo (Ctrl+S) e veja o resultado no painel.
# Mexa só no que está ENTRE as aspas triplas.
# =====================================================================

# ---------------------------------------------------------------------
# NÍVEL 1 - AQUECIMENTO
# ---------------------------------------------------------------------

# Q1. Clientes no Centro
# Colunas do resultado: ClientesNoCentro
Q1 = """
SELECT COUNT(*) AS ClientesNoCentro
FROM Clientes
WHERE Bairro = 'Centro';
"""

# Q2. Hambúrgueres acima de R$ 30
# Colunas do resultado: NomeProduto, Preco
Q2 = """
SELECT NomeProduto, Preco
FROM Produtos
WHERE Categoria = 'Hambúrguer'
AND Preco > 30
ORDER BY Preco DESC;
"""

# Q3. Pedidos por status
# Colunas do resultado: Status, QuantidadePedidos
Q3 = """

"""

# Q4. Nota média e pedidos sem avaliação
# Colunas do resultado: PedidosEntregues, PedidosAvaliados, PedidosSemAvaliacao, NotaMedia
Q4 = """
SELECT
COUNT(*)                 AS PedidosEntregues,
COUNT(Avaliacao)             AS PedidosAvaliados,
COUNT(*) - COUNT(Avaliacao)        AS PedidosSemAvaliacao,
AVG(Avaliacao)   AS NotaMedia
FROM Pedidos
WHERE Status = 'Entregue';
"""

# Q5. Delivery x Retirada por mês
# Colunas do resultado: Mes, TipoEntrega, QuantidadePedidos
Q5 = """
SELECT YEAR(DataPedido) AS AnoPedido,
MONTH(DataPedido) AS Mes, TipoEntrega,
COUNT(*) AS QuantidadePedidos
FROM Pedidos
WHERE Status = 'Entregue' AND TipoEntrega IN ('Delivery', 'Retirada')
GROUP BY YEAR(DataPedido), MONTH(DataPedido), TipoEntrega
ORDER BY YEAR(DataPedido), MONTH(DataPedido), TipoEntrega;


"""

# ---------------------------------------------------------------------
# NÍVEL 2 - CRUZANDO TABELAS
# ---------------------------------------------------------------------

# Q6. Pedidos de janeiro com cliente
# Colunas do resultado: IdPedido, DataPedido, Nome, Bairro, Status
Q6 = """
Select Pedidos.IdPedido, Pedidos.DataPedido, Clientes.Nome, Clientes.Bairro, Pedidos.Status
from Pedidos 
inner join Clientes on Pedidos.IdCliente = Clientes.idCliente
Where Pedidos.DataPedido >= '2026-01-01' and Pedidos.DataPedido < '2026-02-01' 
order by Pedidos.Datapedido asc;


"""

# Q7. Entregas por entregador
# Colunas do resultado: Nome, Entregas
Q7 = """
Select Entregadores.Nome,
count (Pedidos.idPedido) as Quantidade 
from Entregadores 
inner join Pedidos on Entregadores.IdEntregador = Pedidos.IdEntregador
Where Pedidos.Status = 'Entregue' 
Group By Entregadores.Nome 
order by Quantidade desc 

"""

# Q8. Unidades e faturamento por produto
# Colunas do resultado: NomeProduto, UnidadesVendidas, Faturamento
Q8 = """
SELECT Produtos.NomeProduto,
SUM(ItensPedido.Quantidade) AS UnidadesVendidas,
SUM(ItensPedido.Quantidade * ItensPedido.PrecoUnitario) AS  Faturamento
FROM Pedidos
INNER JOIN ItensPedido ON Pedidos.IdPedido = ItensPedido.IdPedido
INNER JOIN Produtos ON ItensPedido.IdProduto = Produtos.IdProduto
WHERE Pedidos.Status = 'Entregue'
GROUP BY Produtos.NomeProduto
ORDER BY UnidadesVendidas DESC;

"""

# Q9. Faturamento por categoria
# Colunas do resultado: Categoria, Faturamento
Q9 = """

SELECT Produtos.Categoria,
SUM(ItensPedido.Quantidade * ItensPedido.PrecoUnitario) AS  Faturamento
FROM Pedidos
INNER JOIN ItensPedido ON Pedidos.IdPedido = ItensPedido.IdPedido
INNER JOIN Produtos ON ItensPedido.IdProduto = Produtos.IdProduto
WHERE Pedidos.Status = 'Entregue'
GROUP BY Produtos.Categoria
ORDER BY  Faturamento DESC;

"""

# Q10. Bairros com 7+ pedidos entregues
# Colunas do resultado: Bairro, PedidosEntregues
Q10 = """

SELECT Clientes.Bairro,
COUNT(*) AS  PedidosEntregues
FROM Pedidos
INNER JOIN Clientes ON Clientes.IdCliente = Pedidos.IdCliente
WHERE Pedidos.Status = 'Entregue'
GROUP BY Clientes.Bairro
HAVING COUNT(*) >= 7;

"""

# Q11. Preços praticados do X-Bacon
# Colunas do resultado: PrecoUnitario, Unidades, Faturamento
Q11 = """

SELECT ItensPedido.PrecoUnitario,
SUM(ItensPedido.Quantidade) AS Unidades,
SUM(ItensPedido.Quantidade * ItensPedido.PrecoUnitario) AS Faturamento
FROM ItensPedido
INNER JOIN Produtos ON ItensPedido.IdProduto = Produtos.IdProduto
INNER JOIN Pedidos ON ItensPedido.IdPedido = Pedidos.IdPedido
WHERE Produtos.NomeProduto = 'X-Bacon' AND Pedidos.Status = 'Entregue'
GROUP BY ItensPedido.PrecoUnitario
ORDER BY ItensPedido.PrecoUnitario ASC; 
"""

# ---------------------------------------------------------------------
# NÍVEL 3 - DESAFIO
# ---------------------------------------------------------------------

# Q12. Top 3 clientes (fidelidade)
# Colunas do resultado: Nome, Pedidos, TotalGasto
Q12 = """
SELECT Clientes.Nome,
COUNT(DISTINCT Pedidos.IdPedido) AS Pedidos,
SUM(ItensPedido.Quantidade * ItensPedido.PrecoUnitario) AS TotalGasto
FROM Clientes
INNER JOIN Pedidos ON Clientes.IdCliente = Pedidos.IdCliente
INNER JOIN ItensPedido ON Pedidos.IdPedido = ItensPedido.IdPedido
WHERE Pedidos.Status = 'Entregue'
GROUP BY Clientes.Nome
ORDER BY TotalGasto DESC;
"""

# Q13. Faturamento mês a mês
# Colunas do resultado: Mes, PedidosEntregues, Faturamento
Q13 = """
SELECT MONTH(Pedidos.DataPedido) AS Mes,
COUNT(DISTINCT Pedidos.IdPedido) AS PedidosEntregues,
SUM(ItensPedido.Quantidade * ItensPedido.PrecoUnitario) AS Faturamento
FROM Pedidos
INNER JOIN ItensPedido ON Pedidos.IdPedido = ItensPedido.IdPedido
WHERE Pedidos.Status = 'Entregue'
GROUP BY MONTH(Pedidos.DataPedido)
ORDER BY Mes ASC;

"""

# Q14. Entregador do trimestre
# Colunas do resultado: Nome, Entregas, NotaMedia
Q14 = """

SELECT Entregadores.Nome,
COUNT(Pedidos.IdPedido) AS Entregas,
CAST(AVG(CAST(Pedidos.Avaliacao AS DECIMAL(10,2))) AS DECIMAL(10,2)) AS NotaMedia
FROM Entregadores
INNER JOIN Pedidos ON Entregadores.IdEntregador = Pedidos.IdEntregador
WHERE Pedidos.Status = 'Entregue'
GROUP BY Entregadores.Nome
HAVING COUNT(Pedidos.IdPedido) >= 4 AND AVG(CAST(Pedidos.Avaliacao AS DECIMAL(10,2))) >= 4;
"""

# Q15. Valor total dos pedidos de março
# Colunas do resultado: IdPedido, Nome, ValorProdutos, TaxaEntrega, ValorTotal
Q15 = """
SELECT Pedidos.IdPedido, Clientes.Nome, Pedidos.TaxaEntrega, 
SUM(ItensPedido.Quantidade * ItensPedido.PrecoUnitario) + Pedidos.TaxaEntrega AS ValorTotal,
SUM(ItensPedido.Quantidade * ItensPedido.PrecoUnitario) AS ValorProdutos
FROM Pedidos
INNER JOIN Clientes ON Pedidos.IdCliente = Clientes.IdCliente
INNER JOIN ItensPedido ON Pedidos.IdPedido = ItensPedido.IdPedido
WHERE Pedidos.Status = 'Entregue' AND Pedidos.DataPedido >= '2026-03-01' AND Pedidos.DataPedido < '2026-04-01'
GROUP BY Pedidos.IdPedido, Clientes.Nome,  Pedidos.TaxaEntrega
ORDER BY ValorTotal DESC;


"""

# Q16. Clientes sem nenhum pedido
# Colunas do resultado: Nome, Bairro, DataCadastro
Q16 = """

"""

# Q17. Produto que nunca foi vendido
# Colunas do resultado: NomeProduto, Categoria, Preco
Q17 = """

"""