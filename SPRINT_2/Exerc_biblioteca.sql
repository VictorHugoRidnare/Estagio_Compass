-- Exercícios de estudo caso "biblioteca"

-- E1
-- Apresente a query para listar todos os livros publicados após 2014. Ordenar pela coluna cod, em ordem crescente, as linhas.  
-- Atenção às colunas esperadas no resultado final: cod, titulo, autor, editora, valor, publicacao, edicao, idioma

select cod, titulo, autor, editora, valor, publicacao, edicao, idioma
from livro
where publicacao >= '2015-01-01'
order by cod

-- E2
-- Apresente a query para listar os 10 livros mais caros. Ordenar as linhas pela coluna valor, em ordem decrescente.  
-- Atenção às colunas esperadas no resultado final:  titulo, valor.

select titulo, valor
from livro
order by valor desc
limit 10

-- E3
-- Apresente a query para listar as 5 editoras com mais livros na biblioteca. 
-- O resultado deve conter apenas as colunas quantidade, nome, estado e cidade. 
-- Ordenar as linhas pela coluna que representa a quantidade de livros em ordem decrescente.

select count(*) as quantidade, nome, estado, cidade 
from livro as liv
join editora as edit 
    on liv.editora = edit.codEditora
join endereco as en
    on edit.endereco = en.codEndereco
group by editora    
order by quantidade desc

-- E4
-- Apresente a query para listar a quantidade de livros publicada por cada autor. 
-- Ordenar as linhas pela coluna nome (autor), em ordem crescente. 
-- Além desta, apresentar as colunas codautor, nascimento e quantidade (total de livros de sua autoria)

SELECT aut.nome, codautor, nascimento, count(liv.autor) AS quantidade
FROM autor as aut
full outer join livro as liv
    on aut.codautor = liv.autor
full outer join editora as edit 
    on liv.editora = edit.codeditora
where aut.nome is not null    
group by aut.nome   
order by aut.nome asc

-- E5
-- Apresente a query para listar o nome dos autores que publicaram livros através de editoras NÃO situadas na região sul do Brasil. 
-- Ordene o resultado pela coluna nome, em ordem crescente. Não podem haver nomes repetidos em seu retorno.

select distinct aut.nome
from autor as aut
join livro as liv 
    on aut.codautor = liv.autor
join editora as edi
    on liv.editora = edi.codEditora
join endereco as en
    on edi.endereco = en.codEndereco
where en.estado NOT in ('PARANÁ', 'RIO GRANDE DO SUL')
order by aut.nome asc


-- E6
-- Apresente a query para listar o autor com maior número de livros publicados. O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes.

select codautor, aut.nome, count(liv.autor) as quantidade_publicacoes
from autor as aut
join livro as liv 
    on aut.codAutor = liv.autor
join editora as edit 
    on liv.editora = edit.codEditora
group by aut.nome
order by quantidade_publicacoes desc
limit 1

-- E7
-- Apresente a query para listar o nome dos autores com nenhuma publicação. Apresentá-los em ordem crescente.
select nome from autor 
where codautor not in (select autor from livro)
order by nome asc