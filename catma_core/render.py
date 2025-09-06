from graphviz import Digraph
from .model import Category

def render_graph(cat: Category, out_path: str = "catma_graph"):
    g = Digraph(comment=cat.name, format="png")
    for o in cat.objects.values():
        g.node(o.id, f"{o.id}\n{', '.join(o.labels)}")
    for m in cat.morphisms.values():
        label = m.kind
        if "weight" in m.attrs: label += f" ({m.attrs['weight']})"
        g.edge(m.src, m.dst, label=label)
    g.render(out_path, cleanup=True)
    return out_path + ".png"
