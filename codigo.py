import csv
import requests
from lxml import html

pagina = requests.get ('https://statusinvest.com.br/acoes/bidi11')
dados = html.fromstring(pagina.content)
indicadorAcoes = dados.xpath('//*[@id="company-section"]/div/div[1]/div[2]/h4/span')

with open('banco_inter_s_a.csv', 'w', newline='') as arquivo:
    final = csv.writer(arquivo, dialect='excel', delimiter=';')
    final.writerow(["Patrimonio Líquido", "Ativos", "Ativo Circulante", "Dívida Bruta", "Disponibilidade", "Dívida Líquida", "Valor de Mercado", "Valor de Firma", "Total de Papeis", "Segmento de Listagem", "Free Float"])
    #dados_linha = dados.xpath('//*[@id="company-section"]/div/div[{}]/div/div/div/strong/text()'.format(cont))
    patrimonio = dados.xpath('//*[@id="company-section"]/div/div[2]/div[1]/div/div/strong/text()')
    print(patrimonio[0])
    
    ativos = dados.xpath('//*[@id="company-section"]/div/div[2]/div[2]/div/div/strong/text()')
    print(ativos[0])
    
    ativo_circulante = dados.xpath('//*[@id="company-section"]/div/div[2]/div[3]/div/div/div/strong/text()')
    print(ativo_circulante)
    
    divida_bruta = dados.xpath('//*[@id="company-section"]/div/div[2]/div[4]/div/div/strong/text()')
    print(divida_bruta)
    
    disponibilidade = dados.xpath('//*[@id="company-section"]/div/div[2]/div[5]/div/div/strong/text()')
    print(disponibilidade)
    
    divida_liquida = dados.xpath('//*[@id="company-section"]/div/div[2]/div[6]/div/div/strong/text()')
    print(divida_liquida)
    
    valor_de_mercado = dados.xpath('//*[@id="company-section"]/div/div[2]/div[7]/div/div/strong/text()')
    print(valor_de_mercado)
    
    valor_de_firma = dados.xpath('//*[@id="company-section"]/div/div[2]/div[8]/div/div/strong/text()')
    print(valor_de_firma)
    
    total_de_papeis = dados.xpath('//*[@id="company-section"]/div/div[2]/div[9]/div/div/strong/text()')
    print(total_de_papeis)
    
    segmento_listagem = dados.xpath('//*[@id="company-section"]/div/div[2]/div[10]/div/div/strong/text()')
    print(segmento_listagem)
    
    free_float = dados.xpath('//*[@id="company-section"]/div/div[2]/div[11]/div/div/strong/text()')
    print(free_float)
    
    final.writerow(str(patrimonio[0])+';'+str(ativos[0])+';'+str(ativo_circulante[0])+';'+str(divida_bruta[0])+';'+str(disponibilidade[0])+';'+str(divida_liquida[0])+';'+str(valor_de_mercado[0])+';'+str(valor_de_firma[0])+';'+str(total_de_papeis[0])+';'+str(segmento_listagem[0])+';'+str(free_float[0]))