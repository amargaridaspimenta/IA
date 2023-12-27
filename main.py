from representacaoEstado import inicializar_estado
from grafo import Grafo
from grafo2 import Grafo2
from grafoUnido import GrafoUnido
from grafoInterativo import GrafoOSMx
from rankingAndaux import imprimir_mensagem_centralizada, top_estafetas_por_avaliacao, top_estafetas_por_entregas
from menuCliente import avaliar_encomenda, criar_encomenda, definir_tempo_e_atribuir_estafeta, visualizar_encomendas_cliente
from menuEstafeta import processar_encomenda, visualizar_perfil_estafeta

def main():
    saida = -1
    grafo_obj = Grafo()
    grafo2_obj = Grafo2()
    grafo_objx = GrafoOSMx()
    estado_inicial = inicializar_estado()

    imprimir_mensagem_centralizada("BEM-VINDO À HEALTH PLANET")

    while saida != 0:
        print("1- Entrar como Cliente")
        print("2- Entrar como Estafeta")
        print("3- Ver Mapas")
        print("0- Sair\n")

        try:
            saida = int(input("Introduza a sua opção:"))
            print()
        except ValueError:
            print("Por favor, insira um valor válido.\n")
            continue 

        if saida == 0:
            print("Obrigado por usar os nossos serviços.")
            print(".....................................\n")

        elif saida == 1:
            while True:
                print()
                print("1- Definir tempo máximo de entrega.")
                print("2- Avaliar encomenda.")
                print("3- Ver Encomendas")
                print("4- Criar encomenda.")
                print("5- Verificar ranking de estafetas com melhor avaliação.")
                print("0- Voltar à página anterior.\n")

                try:
                    clienteSaida = int(input("Introduza a sua opção:"))
                except ValueError:
                    print("Por favor, insira um valor válido.\n")
                    continue 

                if clienteSaida == 0:
                    break
                elif clienteSaida == 1:
                    definir_tempo_e_atribuir_estafeta(estado_inicial)
                elif clienteSaida == 2:
                    avaliar_encomenda(estado_inicial)
                elif clienteSaida == 3:
                    visualizar_encomendas_cliente(estado_inicial)
                elif clienteSaida == 4:
                    criar_encomenda(estado_inicial)
                elif clienteSaida == 5:
                    top_estafetas_por_avaliacao(estado_inicial)

        elif saida == 2:
            while True:
                print()
                print("1- Encomenda a entregar, meio de transporte e caminho")
                print("2- Ver perfil")
                print("3- Verificar ranking de estafetas com mais entregas.")
                print("0- Voltar à página anterior\n")

                try:
                    EstafetaSaida = int(input("Introduza a sua opção:"))
                    print()
                except ValueError:
                    print("Por favor, insira um número válido.")
                    continue 

                if EstafetaSaida == 0:
                    break
                if EstafetaSaida == 0:
                    break
                elif EstafetaSaida == 1:
                    processar_encomenda(estado_inicial,grafo_obj)
                elif EstafetaSaida == 2:
                    visualizar_perfil_estafeta(estado_inicial)
                elif EstafetaSaida == 3:
                    top_estafetas_por_entregas(estado_inicial)

        elif saida == 3:
             while True:
                print()
                print("1- Grafo da Freguesia da Misericórdia (Lisboa)")
                print("2- Grafo da Freguesia de Santa Maria Maior (Lisboa)")
                print("3- Grafo das Freguesias Unidas (Lisboa)")
                print("4- Mapa das Freguesias (Lisboa)")
                print("0- Voltar à página anterior\n")

                try:
                    MapaSaida = int(input("Introduza a sua opção:"))
                    print()
                except ValueError:
                    print("Por favor, insira um número válido.")
                    continue 

                if MapaSaida == 0:
                    break

                elif MapaSaida == 1:
                    grafo_obj.desenha()
                    print("Voltar à página inicial\n")

                elif MapaSaida == 2:
                    grafo2_obj.desenha()
                    print("Voltar à página inicial\n")

                elif MapaSaida == 3:
                    grafo_unido_obj = GrafoUnido()
                    grafo_unido_obj.desenha()
                    print("Voltar à página inicial\n")

                elif MapaSaida == 4:
                    endereco_desejado_osmnx = "Misericórdia, Lisbon, Portugal"
                    ruas_desejadas_osmnx = [
                        'Travessa do Carmo',
                        'Rua do Alecrim',
                        'Travessa de Guilherme Cossoul',
                        'Rua da Horta Sêca',
                        'Rua da Emenda',
                        'Rua das Chagas',
                        'Rua do Ataíde'
                    ]

                    grafo_osmnx = grafo_objx.obter_grafo_osmnx(endereco_desejado_osmnx)
                    # Ajuste do tamanho do mapa aumentado aqui
                    grafo_objx.desenha(grafo_osmnx, ruas_desejadas_osmnx, figsize=(15, 15))

                    print("Voltar à página inicial\n")

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.\n")
            l = input("Prima enter para continuar.")

if __name__ == "__main__":
    main()