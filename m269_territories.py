import matplotlib.pyplot as plot
from m269_ungraph import UndirectedGraph
from m269_digraph import WeightedDiGraph


# plot.margins(x=0.3)
class Territory:
    """A territory for a board game"""

    def __init__(self, territory_name: str, owner: str, armies: int):
        """Initialise name, owner and armies"""
        self.territory_name = territory_name
        self.owner = owner
        self.armies = armies

    def str(self):
        return self.territory_name


# Create the graphs
board_game = UndirectedGraph()
australasia = UndirectedGraph()
australasia_w = WeightedDiGraph()
imagine_w = WeightedDiGraph()

# Create nodes
Alaska = Territory("Alaska", "Phil", 1)
NWTerritory = Territory("NW Territory", "Michel", 1)
Greenland = Territory("Greenland", "Phil", 1)
Alberta = Territory("Alberta", "Brendan", 1)
Ontario = Territory("Ontario", "Adam", 1)
Quebec = Territory("Quebec", "Adam", 1)
WestUS = Territory("Western US", "Brendan", 1)
EastUS = Territory("Eastern US", "Phil", 1)
CentAmerica = Territory("Central America", "Michel", 1)
Venezuela = Territory("Venezuela", "Phil", 1)
Brazil = Territory("Brazil", "Brendan", 1)
Peru = Territory("Peru", "Oli", 1)
Argentina = Territory("Argentina", "Phil", 1)
Iceland = Territory("Iceland", "Adam", 1)
GB = Territory("GB", "Oli", 1)
Scandinavia = Territory("Scandinavia", "Oli", 1)
NEurope = Territory("NEurope", "Adam", 1)
WEurope = Territory("WEurope", "Jane", 1)
SEurope = Territory("SEurope", "Adam", 1)
Ukraine = Territory("Ukraine", "Michel", 1)
MEast = Territory("MEast", "Brendan", 1)
Afghanistan = Territory("Afghanistan", "Jane", 1)
India = Territory("India", "Jane", 1)
Siam = Territory("Siam", "Phil", 1)
China = Territory("China", "Phil", 1)
Ural = Territory("Ural", "Brendan", 1)
Siberia = Territory("Siberia", "Phil", 1)
Yakutsk = Territory("Yakutsk", "Adam", 1)
Irkutsk = Territory("Irkutsk", "Adam", 1)
Mongolia = Territory("Mongolia", "Jane", 1)
Kamchatka = Territory("Kamchatka", "Jane", 1)
Japan = Territory("Japan", "Michel", 1)
Indonesia = Territory("Indonesia", "Jane", 1)
NGuinea = Territory("New Guinea", "Michel", 1)
WAustralia = Territory("Western Australia", "Michel", 2)
EAustralia = Territory("Eastern Australia", "Oli", 1)
NAfrica = Territory("North Africa", "Jane", 1)
Egypt = Territory("Egypt", "Brendan", 1)
EAfrica = Territory("East Africa", "Oli", 1)
Congo = Territory("Congo", "Oli", 1)
SAfrica = Territory("South Africa", "Oli", 1)
Madagascar = Territory("Madagascar", "Brendan", 1)
A = Territory("A", "X", 1)
B = Territory("B", "X", 1)
C = Territory("C", "Z", 1)
D = Territory("D", "Z", 3)
E = Territory("E", "Z", 2)
F = Territory("F", "Z", 2)
G = Territory("G", "Y", 1)

# Add nodes - board_game
board_game.add_node(Alaska)
board_game.add_node(NWTerritory)
board_game.add_node(Greenland)
board_game.add_node(Alberta)
board_game.add_node(Ontario)
board_game.add_node(Quebec)
board_game.add_node(WestUS)
board_game.add_node(EastUS)
board_game.add_node(CentAmerica)
board_game.add_node(Venezuela)
board_game.add_node(Brazil)
board_game.add_node(Peru)
board_game.add_node(Argentina)
board_game.add_node(Iceland)
board_game.add_node(GB)
board_game.add_node(Scandinavia)
board_game.add_node(NEurope)
board_game.add_node(WEurope)
board_game.add_node(SEurope)
board_game.add_node(Ukraine)
board_game.add_node(MEast)
board_game.add_node(Afghanistan)
board_game.add_node(India)
board_game.add_node(Siam)
board_game.add_node(China)
board_game.add_node(Ural)
board_game.add_node(Siberia)
board_game.add_node(Yakutsk)
board_game.add_node(Irkutsk)
board_game.add_node(Mongolia)
board_game.add_node(Kamchatka)
board_game.add_node(Japan)
board_game.add_node(Indonesia)
board_game.add_node(NGuinea)
board_game.add_node(WAustralia)
board_game.add_node(EAustralia)
board_game.add_node(NAfrica)
board_game.add_node(Egypt)
board_game.add_node(EAfrica)
board_game.add_node(Congo)
board_game.add_node(SAfrica)
board_game.add_node(Madagascar)

# Add nodes - australasia
australasia.add_node(Indonesia)
australasia.add_node(NGuinea)
australasia.add_node(WAustralia)
australasia.add_node(EAustralia)
australasia.add_node(Siam)

# Add nodes - australasia_w
australasia_w.add_node(Indonesia)
australasia_w.add_node(NGuinea)
australasia_w.add_node(WAustralia)
australasia_w.add_node(EAustralia)
australasia_w.add_node(Siam)

# Add nodes - imagine_w
imagine_w.add_node(A)
imagine_w.add_node(B)
imagine_w.add_node(C)
imagine_w.add_node(D)
imagine_w.add_node(E)
imagine_w.add_node(F)
imagine_w.add_node(G)

# Add edges - board_game
board_game.add_edge(Alaska, NWTerritory)
board_game.add_edge(Alaska, Kamchatka)
board_game.add_edge(Alaska, Alberta)
board_game.add_edge(NWTerritory, Greenland)
board_game.add_edge(NWTerritory, Alberta)
board_game.add_edge(NWTerritory, Ontario)
board_game.add_edge(Greenland, Iceland)
board_game.add_edge(Greenland, Ontario)
board_game.add_edge(Greenland, Quebec)
board_game.add_edge(Alberta, Ontario)
board_game.add_edge(Alberta, WestUS)
board_game.add_edge(Ontario, Quebec)
board_game.add_edge(Ontario, Greenland)
board_game.add_edge(Quebec, Greenland)
board_game.add_edge(Ontario, EastUS)
board_game.add_edge(Ontario, WestUS)
board_game.add_edge(Quebec, EastUS)
board_game.add_edge(WestUS, EastUS)
board_game.add_edge(WestUS, CentAmerica)
board_game.add_edge(EastUS, CentAmerica)
board_game.add_edge(CentAmerica, Venezuela)
board_game.add_edge(Venezuela, Brazil)
board_game.add_edge(Venezuela, Peru)
board_game.add_edge(Brazil, NAfrica)
board_game.add_edge(Brazil, Argentina)
board_game.add_edge(Brazil, Peru)
board_game.add_edge(Argentina, Peru)
board_game.add_edge(Greenland, Iceland)
board_game.add_edge(Iceland, Scandinavia)
board_game.add_edge(Iceland, GB)
board_game.add_edge(Scandinavia, Ukraine)
board_game.add_edge(Scandinavia, NEurope)
board_game.add_edge(GB, NEurope)
board_game.add_edge(GB, WEurope)
board_game.add_edge(WEurope, NEurope)
board_game.add_edge(WEurope, SEurope)
board_game.add_edge(WEurope, NAfrica)
board_game.add_edge(NEurope, Ukraine)
board_game.add_edge(NEurope, SEurope)
board_game.add_edge(SEurope, Ukraine)
board_game.add_edge(SEurope, MEast)
board_game.add_edge(SEurope, Egypt)
board_game.add_edge(SEurope, NAfrica)
board_game.add_edge(Ukraine, Ural)
board_game.add_edge(Ukraine, Afghanistan)
board_game.add_edge(Ukraine, MEast)
board_game.add_edge(NAfrica, Egypt)
board_game.add_edge(NAfrica, EAfrica)
board_game.add_edge(NAfrica, Congo)
board_game.add_edge(Congo, EAfrica)
board_game.add_edge(Congo, SAfrica)
board_game.add_edge(SAfrica, EAfrica)
board_game.add_edge(SAfrica, Madagascar)
board_game.add_edge(Madagascar, EAfrica)
board_game.add_edge(EAfrica, MEast)
board_game.add_edge(EAfrica, Egypt)
board_game.add_edge(Egypt, MEast)
board_game.add_edge(MEast, Afghanistan)
board_game.add_edge(MEast, India)
board_game.add_edge(Ural, Siberia)
board_game.add_edge(Ural, China)
board_game.add_edge(Ural, Afghanistan)
board_game.add_edge(Afghanistan, China)
board_game.add_edge(Afghanistan, India)
board_game.add_edge(India, China)
board_game.add_edge(India, Siam)
board_game.add_edge(Siberia, Yakutsk)
board_game.add_edge(Siberia, Irkutsk)
board_game.add_edge(Siberia, Mongolia)
board_game.add_edge(Siberia, China)
board_game.add_edge(China, Mongolia)
board_game.add_edge(China, Siam)
board_game.add_edge(Yakutsk, Kamchatka)
board_game.add_edge(Yakutsk, Irkutsk)
board_game.add_edge(Irkutsk, Kamchatka)
board_game.add_edge(Irkutsk, Mongolia)
board_game.add_edge(Mongolia, Kamchatka)
board_game.add_edge(Mongolia, Japan)
board_game.add_edge(Kamchatka, Japan)
board_game.add_edge(Siam, Indonesia)
board_game.add_edge(Indonesia, NGuinea)
board_game.add_edge(Indonesia, WAustralia)
board_game.add_edge(NGuinea, EAustralia)
board_game.add_edge(NGuinea, WAustralia)
board_game.add_edge(WAustralia, EAustralia)

# Add edges - australasia
australasia.add_edge(Indonesia, NGuinea)
australasia.add_edge(Indonesia, WAustralia)
australasia.add_edge(NGuinea, EAustralia)
australasia.add_edge(NGuinea, WAustralia)
australasia.add_edge(WAustralia, EAustralia)
australasia.add_edge(Indonesia, Siam)

# Add edges - australasia_w
australasia_w.add_edge(WAustralia, EAustralia, EAustralia.armies)
australasia_w.add_edge(Indonesia, WAustralia, WAustralia.armies)
australasia_w.add_edge(NGuinea, EAustralia, EAustralia.armies)
australasia_w.add_edge(Indonesia, NGuinea, NGuinea.armies)
australasia_w.add_edge(Siam, Indonesia, Siam.armies)
australasia_w.add_edge(NGuinea, WAustralia, WAustralia.armies)

# Add edges - imagine_w
imagine_w.add_edge(B, C, 3)
imagine_w.add_edge(A, D, 9)
imagine_w.add_edge(A, G, 3)
imagine_w.add_edge(D, E, 3)
imagine_w.add_edge(E, D, 9)
imagine_w.add_edge(G, E, 3)
imagine_w.add_edge(E, G, 3)
imagine_w.add_edge(B, D, 6)
imagine_w.add_edge(E, F, 6)


# Test edges (optional): Print some sample connections
print("\n**Sample Connections (Board Game):**")
for territory, neighbours in board_game.out.items():
    if len(neighbours) > 0:
        print(
            f"- {territory.territory_name} connected to: {', '.join([n.territory_name for n in neighbours])}"
        )

# Optional: Visualization using networkx (requires networkx library)
try:
    import networkx as nx

    # Convert board_game to a networkx graph
    G = nx.Graph()
    for territory in board_game.nodes():
        G.add_node(territory.territory_name)

    for start, neighbours in board_game.out.items():
        for neighbour in neighbours:
            G.add_edge(start.territory_name, neighbour.territory_name)

    # Draw the graph visually (requires matplotlib as well)
    nx.draw(G, with_labels=True, font_weight="bold")
    plot.show()

except ImportError:
    print(
        "\n**Note:** Visualization requires networkx library. Install using 'pip install networkx'."
    )
