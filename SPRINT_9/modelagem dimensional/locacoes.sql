--Dimensão Locação

CREATE VIEW dim_Locacao AS 
SELECT idLocacao as locacao,
		idCliente as cliente,
		idCarro as carro,
		dataLocacao as data_locacao,
		qtdDiaria as qtd_diaria,
		vlrDiaria as valor_diaria,
		dataEntrega as dt_entrega,
		horaEntrega as hr_entrega,
		idVendedor as vendedor
FROM Locacoes l 

--Dimensão Cliente
CREATE VIEW dim_cliente as
SELECT idCliente as cliente,
		nomeCliente as nome_cliente,
		cidadeCliente as cidade_cliente,
		estadoCliente as estado_cliente,
		paisCliente as pais_cliente
FROM Clientes c 


--Dimensão Carros
CREATE VIEW dim_carros AS
SELECT idCarro as carro,
		kmCarro as kilometragem,
		classiCarro as classi_carro,
		marcaCarro as marca,
		modeloCarro as modelo,
		anoCarro as ano_carro,
		idCombustivel as combustivel_carro
FROM Carros c 

--Dimensão combustíveis
CREATE VIEW dim_combustiveis AS
SELECT idCombustivel as combustivel,
		tipoCombustivel as tipo
FROM Combustiveis c 

--Dimensão Vendedores
CREATE VIEW dim_vendedores AS 
SELECT 
	idVendedor as vendedor,
	nomeVendedor as nome,
	sexoVendedor as sexo,
	estadoVendedor as estado_vendedor
FROM Vendedores v 