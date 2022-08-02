# Health Insurance Cross Sell

## Contexto do problema

O nosso cliente é uma seguradora que forneceu Seguro Saúde para seus clientes, agora eles precisam de ajuda na construção de um modelo para prever se os segurados (clientes) do ano passado também terão interesse no Seguro Automóvel oferecido pela empresa.

![How-health-insurance-](https://user-images.githubusercontent.com/81040797/146363458-13cb65b7-c42a-42dc-bd86-24b4eec1aae4.jpg)

## Estrutura da Solução

1. Descrição dos dados
2. Feature engeneering
3. Análise exploratória
4. Preparação dos dados
5. Feature selection
6. Machine Leearning modeling
7. Model performance
8. Publicação do modelo em produção

## Premissas Assumidas
1. A intenção de adquirir o seguro automóvel é diretamente influenciada pelo fato do cliente já possuir seguro saúde.
2. A venda cruzada aumenta a fidelidade dos clientes.
3. Um modelo de Machine Learning que consiga fazer o Rankeamento dos clientes mais propensos a adiquirir o seguro automóvel pode reduzir os custos de venda.

## Insights
### Clientes do sexo feminino deveriam ter mais interesse em adquirir o seguro do que cliente do sexo masculino
**Falso**. Apenas **10,4%** dos cliente do genero feminino tem interesse em adquirir o seguro, já **13,84%** dos cliente do genero masculino possuem interesse
![image](https://user-images.githubusercontent.com/81040797/146605510-2755ca8b-e5df-4df8-b041-a74067fc2c6b.png)

### Clientes mais velhos devem ter mais interesse em adquirir o seguro do que clientes mais jovens
**Verdadeiro.** Clientes acima 35 anos representam **73,18%** dos clientes que possuem interesse em adquirir o seguro.
![image](https://user-images.githubusercontent.com/81040797/146624726-3f84da3f-9787-4522-9144-45ff2ec64222.png)


### Clientes com Veiculos mais novos possuem mais interesse em adquirir o seguro
**Falso.**
- Dos clientes que possuem carros novos **4,37%** possuem interesse.
- Dos clientes que possuem carros usados **29,39%** possuem interesse.
- Dos clientes que possuem carros velhos **17,37%.**

![image](https://user-images.githubusercontent.com/81040797/146606750-29b46b99-45f1-4625-ae1c-d1890c7bc5ab.png)

## Machine Learning Performance

No modelo de Regressão Linear com **20%** da base ordenada é possível alcançar **45%** dos clientes interessados e com **50%** da base ordenada é possível alcançar praticamente **100%** dos clientes interessados

![image](https://user-images.githubusercontent.com/81040797/147998688-e34bf4dd-54f9-4759-ba79-512632f01aa8.png)

## Conclusão, Precision e Recall

Sem o ranqueamento gerado pelo modelo, a empresa teria que entrar em contato com os clientes de forma aleatória para obter o maior número possível de clientes que tenham interesse no seguro automóvel. Porém, com os clientes raqueados, a empresa poderia direcionar as suas ações para os clientes propensos a aquisição do produto, segundo as sugestões realizadas pelo modelo, de forma a otimizar o tempo disponibilizado, reduzir os recursos empregados, bem como maximizar a receita.

Base de dados: 76.000 clientes.

Entrando em contato com 17.000 clientes rankeados é possivel compreender 51% dos clientes interessados no seguro com uma precisão de 28%.

- Precision at K:  0.280512911005235
- Recall at K:     0.5146773149147421

Entrando em contato com 30.000 clientes rankeados é possivel compreender 86% dos clientes interessados no seguro com uma precisão de 26,7%.

- Precision at K:  0.2674244191860271
- Recall at K:     0.8628737362873736

![image](https://user-images.githubusercontent.com/81040797/147999210-724e9b41-7ed1-40b7-8e82-b4407069e7c0.png)

## Próximos Passos

No próximo cliclo é possível utilizar algoritmos de machine laerning mais elaborados que pudessem compreender melhor os dados de maneira a aumentar a precisão e o recall do modelo dentro do menor número possível de clientes.
