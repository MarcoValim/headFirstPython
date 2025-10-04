from string import Template

""" Esta função aceita uma string (opcional) como seu único argumento e usa-a para criar uma linha CGI "Content type:" com "text/html" como padrão."""
def start_response(resp="text/html"):
    return('Content-type ' + resp + '\n\n')

"""Esta função aceita uma única string como seu argumento e usa no título para o começo de uma página HTML. A página em si é armazenada em um arquivo separado em "template/header.html" e o título é substituído quando necessário."""
def include_header(the_title):
    with open('template/header.html') as headf:
        head_text = headf.read()
    header = Template(head_text)
    return(header.substitute(title=the_title))

"""Semelhante à função "include_header" esta usa a sua única string como semente para criar o final de uma página HTML. A página em si é armazenada em um arquivo separado em "templates/footer.html" e o argumento é usado para criar dinamicamente um conjunto de tags de linh HTML. Com base em como são usadas, parece que o argumento precisa ser um dicionpario."""
def include_footer(the_links):
    with open('template/header.html') as footf:
        foot_text = footf.read()
    link_string = '' 
    for key in the_links:
        link_string += '<a href="' + the_links[key] + '">' + key + '</a>&nbsp;&nbsp;&nbsp;&nbsp;'
    footer = Template(foot_text)
    return(footer.substitute(links=link_string))

"""Essa função retorna o HTML para o início de um formulário e permite que quem a chama especifique a URL para enviar os dados do formulário, bem como o método utiliza."""
def start_form(the_url, form_type = "POST"):
    return('<form action="' + the_url + '" method="' + form_type + '">')

"""Esta função retorna a marcação HTML que encerra o formulário, permitindo que quem a chama personalize o texto do formulário com o botão "submit"."""
def end_form(submit_msg="Submit"):
    return('<p></p><input type=submit value"' + submit_msg + '">')

"""Dado um nome e um valor de botão de opção, crie um botão de opção em HTML (tipicamente incluído em formulários HTML). Observação: ambos os argumentos são necessários."""
def radio_button(rb_name, rb_value):
    return('<input type = "radio" name="' + rb_name + '"value"' + rb_value + '"> ' + rb_value + '<br />')

"""Dada uma lista de itens, esta função transforma a lista em uma lista não numerada HTML. Um simples loop "for" faz todo o trabalho, adicionando LI ao elemento UL em cada iteração."""
def u_list(items):
    u_string = '<ul>'
    for item in items:
        u_string += '<li>' + item + '</li>'
    u_string += '</ul>'
    return(u_string)

"""Crie e retorne a uma tag do cabeçalho HTML (H1, H2, H3 e assim por diante) com o nível 2 como padrão. O argumento "header_text" é necessário."""
def header(header_text, header_level=2):
    return('<h' + str(header_level) + '>' + header_text + '</h' + str(header_level) + '>')

""" Coloque um parágrafo de texto (uma string) entre as tags do parágrafo HTML."""    
def para(para_text):
     return('<p>' + para_text + '</p>')
     
