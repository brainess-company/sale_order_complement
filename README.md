# Customização de Campos em Cotações do Odoo

Este módulo personalizado adiciona os campos **NCM** e **Marca (Brand)** às seguintes áreas do Odoo:

1. **Visualização no Portal do Cliente**: Inclui os campos na tela onde o cliente visualiza a cotação enviada por link.
2. **Relatório Impresso (PDF)**: Adiciona os campos ao relatório de cotação exportado ou impresso.
3. **Linhas da Cotação no Backend**: Exibe os campos nas linhas da cotação na interface administrativa do Odoo.

## Estrutura do Módulo

### Arquivos Incluídos

- **`__init__.py`**: Inicializa os diretórios e importa os arquivos necessários.
- **`__manifest__.py`**: Define as dependências e as configurações do módulo.
- **`models/sale_order_line.py`**: (Opcional) Define campos adicionais para o modelo `sale.order.line`, caso os campos NCM e Marca não estejam disponíveis.
- **`views/portal_sale_order_template.xml`**: Personaliza a visualização do portal do cliente para incluir os campos NCM e Marca.
- **`views/report_sale_order.xml`**: Modifica o relatório PDF de cotação para exibir os campos NCM e Marca.
- **`views/sale_order_line_views.xml`**: (Opcional) Adiciona os campos à interface administrativa do Odoo.

## Configuração

### 1. Dependências

Certifique-se de que os seguintes módulos estejam instalados no seu ambiente:

- `l10n_br_fiscal`: Para o suporte ao campo **NCM**.
- `product_brand`: Para o suporte ao campo **Marca** (Brand).

### 2. Instalação

1. Copie o módulo para o diretório `addons` do seu Odoo.
2. Atualize a lista de aplicativos no Odoo.
3. Instale o módulo personalizado.

## Personalizações

### Portal do Cliente

O template `portal_sale_order_template` foi herdado para incluir os campos NCM e Marca na tabela de itens da cotação. Os valores são exibidos dinamicamente a partir das informações do produto.

### Relatório PDF

O template `sale.report_saleorder_document` foi modificado para incluir as novas colunas **NCM** e **Marca** na tabela de itens do relatório PDF.

### Backend (Interface Administrativa)

As linhas de cotação no backend exibem os campos NCM e Marca como campos adicionais na tabela de produtos.

## Notas

1. **Caso os Campos Já Existam:** Se os campos NCM e Marca já estiverem configurados nos modelos do Odoo, os arquivos Python e as definições em `models/` podem ser omitidos.
2. **Modo Desenvolvedor:** Ative o modo desenvolvedor no Odoo para verificar se os campos estão disponíveis antes de criar os modelos customizados.

## Suporte

Se encontrar problemas ou tiver dúvidas, entre em contato com o administrador do sistema ou o desenvolvedor responsável pelo módulo.

