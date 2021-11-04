#include <bits/stdc++.h>
using namespace std;

#define MAXIMO 0x3f3f3f3f

typedef pair<int, int> iPair;

class Grafo {
    int V;

    list<pair<int, int>> *listaAdjacencias;

    public:
    Grafo(int V);

    void addAresta(int u, int v, int peso);

    void primMST(int origem);

    void imprimirMST(vector<int> MST);
};