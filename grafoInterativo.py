import osmnx as ox
import geopandas as gpd
import matplotlib.pyplot as plt

class GrafoOSMx:
    def obter_grafo_osmnx(self, address):
        g = ox.graph_from_address(address, network_type="drive")
        return g

    def desenha(self, g=None, ruas_desejadas=None, figsize=(12, 12)):
        if g is not None:
            gdf_edges = ox.graph_to_gdfs(g, nodes=False, edges=True)

            # filtra as ruas que pretendemos
            gdf_ruas_desejadas = gdf_edges[gdf_edges['name'].isin(ruas_desejadas)]

            # remove os nomes duplicados das ruas
            gdf_ruas_desejadas = gdf_ruas_desejadas.drop_duplicates(subset='name')

            gdf_mapa = gpd.GeoDataFrame(geometry=gdf_ruas_desejadas['geometry'])

            fig, ax = plt.subplots(figsize=figsize)
            gdf_mapa.plot(ax=ax, color='red', linewidth=2, alpha=0.5)

            ox.plot_graph(g, ax=ax, node_size=0, edge_color='k', edge_linewidth=0.5, bgcolor='white', show=False)

            for idx, row in gdf_ruas_desejadas.iterrows():
                x = row['geometry'].centroid.x
                y = row['geometry'].centroid.y
                plt.text(x, y, f"{row['name']} - Length: {row['length']:.2f} Km", fontsize=8, ha='center', va='center', color='blue', rotation=0)

            # ajusta os eixos
            ax.set_aspect('equal', adjustable='datalim')

            plt.title("Mapa da Freguesia da Misericórdia (Lisboa)")
            plt.draw()
            plt.show()
        else:
            print("Grafo não fornecido.")

grafo_draw = GrafoOSMx()

#endereco_desejado = "Travessa do Carmo, Lisbon, Portugal"

#grafo_osmnx = grafo_draw.obter_grafo_osmnx(endereco_desejado)

# lista das ruas
ruas_desejadas = [
    'Travessa do Carmo',
    'Rua do Alecrim',
    'Travessa de Guilherme Cossoul',
    'Rua da Horta Sêca',
    'Rua da Emenda',
    'Rua das Chagas',
    'Rua do Ataíde'
]

#grafo_draw.desenha(grafo_osmnx, ruas_desejadas, figsize=(15, 15))
