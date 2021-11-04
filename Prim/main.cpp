#include "primMST.h"

int main(void)
{
    // create the graph given in above fugure
    int V = 6;
    Grafo g(V);

    //  making above shown graph
    g.addAresta(3,4,8);
    g.addAresta(4,5,-1);
    g.addAresta(3,2,6);
    g.addAresta(3,0,3);
    g.addAresta(2,0,1);
    g.addAresta(2,5,5);
    g.addAresta(0,1,2);
    g.addAresta(1,5,4);

    g.primMST(4);

    return 0;
}