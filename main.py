from representacaoEstado import inicializar_estado
from grafo import Grafo
from grafoInterativo import GrafoOSMx
from rankingAndaux import imprimir_mensagem_centralizada, top_estafetas_por_avaliacao, top_estafetas_por_entregas
from menuCliente import avaliar_encomenda, criar_encomenda, definir_tempo_e_atribuir_estafeta, visualizar_encomendas_cliente
from menuEstafeta import processar_encomenda, visualizar_perfil_estafeta

                                                                        ###########
                                                                        #   Main  #
                                                                        ###########

def main():
    saida = -1
    endereco = "Freguesia da Misericordia, Lisbon, Portugal"
    grafo_objx = GrafoOSMx(endereco)
    grafo_obj = Grafo()
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
                    processar_encomenda(estado_inicial,grafo_obj, grafo_objx)
                elif EstafetaSaida == 2:
                    visualizar_perfil_estafeta(estado_inicial)
                elif EstafetaSaida == 3:
                    top_estafetas_por_entregas(estado_inicial)

        elif saida == 3:
             while True:
                print()
                print("1- Mapa da Freguesia da Misericórdia (Lisboa)")
                print("2- Grafo de Ruas da Freguesia da Misericórdia (Lisboa)")
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
                    grafo_objx.desenha_freguesia()
                    print("Voltar à página inicial\n")

                elif MapaSaida == 2:
                    grafo_obj.desenha_ruas()
                    print("Voltar à página inicial\n")

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.\n")
            l = input("Prima enter para continuar.")

if __name__ == "__main__":
    main()