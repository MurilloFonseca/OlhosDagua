define p = Character('Protagonista')
define a = Character('Ana')
define m = Character('Maria')
define d = Character('Duzu')
define v = Character('Dorvi')


label chapTitle(title):
    scene black
    centered "{size=+30}[title]"
    with dissolve

    return

label start:
    scene black 
    show bg cap 0
    "A vida aqui é dura, e cada dia traz novos desafios."

    "Sob o peso da chuva e das ameaças constantes,
    os olhos são testemunhas de histórias que nunca deveriam ter sido contadas."
    
    jump chap1


label chap1:
    call chapTitle("Olhos d'Água") from _call_chapTitle
    show bg cap 1
    
    p "Eu me lembro de tantas coisas...\n"
    p "A brincadeira de 'Rainha', as tempestades que assustavam minha mãe...\n"
    extend "mas a cor de seus olhos..."
    p "Por que não consigo lembrar?"

    menu:
        "Lembrar das brincadeiras de infância":
            show bg cap 1 1
            " "
        "Pensar na jornada de volta":
            show bg cap 1 23
            " "

    p "Minha mãe... "
    extend "meus ancestrais...\n"
    extend "sinto a presença deles"
    p "Mas ao mesmo tempo, estou tão longe..."

    menu:
        "Refletir sobre o significado da viagem":
            show bg cap 1 23
            " "
        "Questionar o que significa 'olhos d'água'":
            show bg cap 1 4
            " "

    pause 0.5
    jump chap2


label chap2:
    call chapTitle("Ana Davenga") from _call_chapTitle_1
    show bg cap 2 

    a "Davenga é duro, mas eu conheço sua alma."
    a "Ele chora quando estamos sozinhos, e é nesses momentos que vejo quem ele realmente é."

    menu:
        "Lembrar de como se conheceram":
            show bg cap 2 1
            " "
        "Pensar no futuro com Davenga":
            show bg cap 2 2

    a "Este barraco é nosso refúgio, mas também é uma prisão."
    a "Aqui, somos amados e odiados.\n"
    extend "Respeitados e temidos."

    menu:
        "Refletir sobre a vida na favela":
            show bg cap 2 34
            " "
        "Recordar as noites de festa":
            show bg cap 2 34
            " "
    
    pause 0.5
    jump chap3


label chap3:
    call chapTitle('Maria') from _call_chapTitle_2
    show bg cap 3
    
    m "Eu só queria voltar para casa, para os meus filhos.\n" 
    extend "O cansaço pesa, mas o amor por eles me mantém de pé."

    menu:
        "Relembrar a infância":
            show bg cap 3 12
            " "
        "Pensar no futuro dos filhos":
            show bg cap 3 12
            " "
    
    m "No ônibus, reencontrei o pai do meu primeiro filho...\n"
    extend "e logo depois, ele assaltou todos os passageiros."

    menu:
        "Refletir sobre o passado com ele":
            show bg cap 3 34
            " "
        "Pensar na brutalidade e no monstro que ele se tornou":
            show bg cap 3 34
            " "

    pause 0.5
    jump chap4


label chap4:
    call chapTitle("Duzu Querença") from _call_chapTitle_3
    show bg cap 4
    
    d "Minha vida foi um longo pesadelo...\n"
    extend "tantos filhos perdidos, tantas lutas em vão."

    menu:
        "Recordar a infância":
            show bg cap 4 1
            " "
        "Refletir sobre os netos":
            show bg cap 4 2
            " "

    d "A vida nas ruas me transformou em algo que nunca pensei que seria.\n"
    extend "Mas, às vezes, nos delírios, ainda encontro um pouco de paz."

    menu:
        "Lembrar dos dias no bordel":
            show bg cap 4 34
            " "
        "Refletir sobre a morte de Tático":
            show bg cap 4 34
            " " 

    pause 0.5
    jump chap5


label chap5:
    call chapTitle("A Gente Combinamos de Não Morrer") from _call_chapTitle_4
    show bg cap 5
    
    v "Nós prometemos não morrer...\n"
    extend "mas como cumprir essa promessa quando a morte nos ronda a cada esquina?"

    menu:
        "Lembrar da infância":
            show bg cap 5 1
            " "
        "Pensar no futuro da família":
            show bg cap 5 2
            " "

    v "A violência está enraizada em nossas vidas.\n"
    extend "Ela nos define"
    extend ", nos molda"
    extend ", nos destrói."

    menu:
        "Refletir sobre a violência":
            show bg cap 5 34
            " "
        "Pensar na fuga":
            show bg cap 5 34
            " "

    pause 0.5
    jump epilogo

label epilogo:
    show bg epilogo

    "Nossos olhos d'água são testemunhas de nossas histórias.\n"
    "Eles choram, mas também brilham, como um rio que, mesmo ferido, continua a fluir."

    call chapTitle('FIM') from _call_chapTitle_5
    return


